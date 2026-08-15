from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import rasterio
from rasterio.transform import from_origin
from rasterio.merge import merge
from rasterio.mask import mask
from shapely.geometry import box, mapping

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUTS = ROOT / "outputs"
DATA.mkdir(exist_ok=True)
OUTPUTS.mkdir(exist_ok=True)

rng = np.random.default_rng(42)
crs = "EPSG:32617"
res = 10
height = width = 100

# Build two adjacent synthetic raster tiles with consistent metadata.
for i, x0 in enumerate([500000, 501000], start=1):
    arr = rng.normal(loc=0.45 + i * 0.03, scale=0.08, size=(height, width)).astype("float32")
    arr = np.clip(arr, 0, 1)
    arr[rng.random(arr.shape) < 0.02] = -9999
    transform = from_origin(x0, 2800000, res, res)
    path = DATA / f"tile_{i}.tif"
    with rasterio.open(
        path,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=1,
        dtype="float32",
        crs=crs,
        transform=transform,
        nodata=-9999,
    ) as dst:
        dst.write(arr, 1)

paths = sorted(DATA.glob("tile_*.tif"))
rows = []
srcs = []
for path in paths:
    src = rasterio.open(path)
    srcs.append(src)
    band = src.read(1)
    valid = band[band != src.nodata]
    rows.append({
        "file": path.name,
        "crs": str(src.crs),
        "resolution_x": src.res[0],
        "resolution_y": src.res[1],
        "dtype": src.dtypes[0],
        "nodata": src.nodata,
        "valid_min": float(valid.min()),
        "valid_max": float(valid.max()),
        "valid_mean": float(valid.mean()),
        "nodata_pct": float((band == src.nodata).mean() * 100),
    })

qa = pd.DataFrame(rows)
qa.to_csv(OUTPUTS / "input_qaqc.csv", index=False)

# Fail early if key grid properties are inconsistent.
assert qa["crs"].nunique() == 1, "CRS mismatch detected"
assert qa[["resolution_x", "resolution_y"]].drop_duplicates().shape[0] == 1, "Resolution mismatch detected"
assert qa["dtype"].nunique() == 1, "Raster dtype mismatch detected"

mosaic, transform = merge(srcs, nodata=-9999)
meta = srcs[0].meta.copy()
meta.update({
    "height": mosaic.shape[1],
    "width": mosaic.shape[2],
    "transform": transform,
    "compress": "deflate",
})

mosaic_path = OUTPUTS / "mosaic.tif"
with rasterio.open(mosaic_path, "w", **meta) as dst:
    dst.write(mosaic)

# Clip a smaller AOI from the mosaic.
aoi = box(500250, 2799250, 501750, 2799950)
with rasterio.open(mosaic_path) as src:
    clipped, clipped_transform = mask(src, [mapping(aoi)], crop=True)
    clipped_meta = src.meta.copy()
    clipped_meta.update({
        "height": clipped.shape[1],
        "width": clipped.shape[2],
        "transform": clipped_transform,
        "compress": "deflate",
    })

analysis_path = OUTPUTS / "analysis_ready_clip.tif"
with rasterio.open(analysis_path, "w", **clipped_meta) as dst:
    dst.write(clipped)

valid = clipped[0][clipped[0] != -9999]
report = {
    "input_tiles": len(paths),
    "crs": crs,
    "resolution_m": res,
    "analysis_ready_file": analysis_path.name,
    "valid_pixels": int(valid.size),
    "minimum": float(valid.min()),
    "maximum": float(valid.max()),
    "mean": float(valid.mean()),
    "nodata_pct": float((clipped[0] == -9999).mean() * 100),
    "checks": {
        "consistent_crs": True,
        "consistent_resolution": True,
        "consistent_dtype": True,
        "expected_range_0_to_1": bool((valid.min() >= 0) and (valid.max() <= 1)),
    },
}
(OUTPUTS / "qa_report.json").write_text(json.dumps(report, indent=2))

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
axes[0].imshow(mosaic[0], cmap="viridis", vmin=0, vmax=1)
axes[0].set_title("Mosaicked raster")
axes[0].axis("off")
axes[1].imshow(clipped[0], cmap="viridis", vmin=0, vmax=1)
axes[1].set_title("Analysis-ready AOI")
axes[1].axis("off")
fig.suptitle("Raster ETL and QA/QC quick look")
fig.tight_layout()
fig.savefig(OUTPUTS / "quicklook.png", dpi=180)
plt.close(fig)

for src in srcs:
    src.close()

print(json.dumps(report, indent=2))
