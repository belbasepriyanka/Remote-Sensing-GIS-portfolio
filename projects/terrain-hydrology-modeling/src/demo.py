from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

rng = np.random.default_rng(12)
ny, nx = 180, 220
y, x = np.mgrid[0:ny, 0:nx]

dem = (
    420
    + 0.9 * (ny - y)
    + 0.35 * x
    + 32 * np.sin(x / 24)
    + 20 * np.cos(y / 27)
    + rng.normal(0, 1.5, size=(ny, nx))
)

# Add a broad valley to create a realistic drainage tendency.
valley = 55 * np.exp(-((x - (0.58 * nx + 0.22 * y)) ** 2) / (2 * 18**2))
dem = dem - valley

# Slope in degrees from grid-cell gradients.
dy, dx = np.gradient(dem)
slope_deg = np.degrees(np.arctan(np.hypot(dx, dy)))

# Basic D8 routing: each cell points to the steepest lower neighbor.
offsets = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
receiver = np.full((ny, nx, 2), -1, dtype=int)
for r in range(1, ny-1):
    for c in range(1, nx-1):
        best_drop = 0.0
        best = None
        z = dem[r, c]
        for dr, dc in offsets:
            nr, nc = r + dr, c + dc
            dist = np.sqrt(2) if dr and dc else 1.0
            drop = (z - dem[nr, nc]) / dist
            if drop > best_drop:
                best_drop = drop
                best = (nr, nc)
        if best is not None:
            receiver[r, c] = best

# Accumulate contributing cells in descending elevation order.
acc = np.ones((ny, nx), dtype=float)
order = np.dstack(np.unravel_index(np.argsort(dem.ravel())[::-1], dem.shape))[0]
for r, c in order:
    nr, nc = receiver[r, c]
    if nr >= 0:
        acc[nr, nc] += acc[r, c]

threshold = np.percentile(acc, 98.7)
streams = acc >= threshold

summary = {
    "elevation_min": float(dem.min()),
    "elevation_max": float(dem.max()),
    "mean_slope_deg": float(slope_deg.mean()),
    "maximum_flow_accumulation_cells": float(acc.max()),
    "stream_threshold_cells": float(threshold),
    "stream_proxy_pixels": int(streams.sum()),
    "note": "Synthetic DEM demonstration; production hydrology requires validated depression treatment and watershed methods."
}
(OUTPUTS / "summary.json").write_text(json.dumps(summary, indent=2))

fig, axes = plt.subplots(1, 3, figsize=(13, 4.3))
im0 = axes[0].imshow(dem, cmap="terrain")
axes[0].set_title("Synthetic DEM")
axes[0].axis("off")
fig.colorbar(im0, ax=axes[0], fraction=0.046)
im1 = axes[1].imshow(slope_deg, cmap="magma")
axes[1].set_title("Slope (degrees)")
axes[1].axis("off")
fig.colorbar(im1, ax=axes[1], fraction=0.046)
axes[2].imshow(np.log1p(acc), cmap="Blues")
axes[2].contour(streams, levels=[0.5], colors="black", linewidths=0.8)
axes[2].set_title("Flow accumulation + stream proxy")
axes[2].axis("off")
fig.suptitle("Terrain and Hydrology Modeling Workflow")
fig.tight_layout()
fig.savefig(OUTPUTS / "terrain_hydrology_quicklook.png", dpi=180)
plt.close(fig)

print(json.dumps(summary, indent=2))
