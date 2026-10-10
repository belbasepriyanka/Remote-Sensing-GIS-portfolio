"""Vector geometry, attribute and polygon coverage QA with machine-readable reports."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely import normalize, union_all
from shapely.validation import explain_validity


def validate(gdf, required=(), class_field=None, allowed=(), boundary=None, area_crs=None):
    """Return summary and feature issues without modifying source geometry.

    Topology areas require an explicitly supplied projected CRS in metres.
    Gaps are meaningful only against a supplied authoritative coverage boundary.
    """
    issues = []
    def issue(row, code, detail):
        issues.append({'row': int(row), 'code': code, 'detail': str(detail)})
    gdf = gdf.reset_index(drop=True)
    usable = []
    seen = {}
    for i, geom in enumerate(gdf.geometry):
        if geom is None:
            issue(i, 'NULL_GEOMETRY', 'Missing geometry')
        elif geom.is_empty:
            issue(i, 'EMPTY_GEOMETRY', 'Empty geometry')
        elif not geom.is_valid:
            issue(i, 'INVALID_GEOMETRY', explain_validity(geom))
        else:
            key = normalize(geom).wkb
            if key in seen:
                issue(i, 'DUPLICATE_GEOMETRY', f'Duplicates row {seen[key]}')
            else:
                seen[key] = i
            usable.append(i)
    for field in required:
        if field not in gdf:
            issue(-1, 'MISSING_FIELD', field)
            continue
        missing = gdf[field].isna() | gdf[field].astype(str).str.strip().eq('')
        for i in gdf.index[missing]:
            issue(i, 'MISSING_ATTRIBUTE', field)
    if class_field:
        if class_field not in gdf:
            issue(-1, 'MISSING_FIELD', class_field)
        elif allowed:
            for i in gdf.index[~gdf[class_field].astype(str).isin(allowed)]:
                issue(i, 'INVALID_CLASS', f'{class_field}={gdf.at[i, class_field]}')
    if gdf.crs is None:
        issue(-1, 'MISSING_CRS', 'Cannot establish spatial units or alignment')
    topology = {'checked': False}
    if area_crs:
        if gdf.crs is None:
            raise ValueError('Input must declare its source CRS before topology analysis')
        projected = gdf.loc[usable].to_crs(area_crs)
        if not projected.crs.is_projected or any(a.unit_name != 'metre' for a in projected.crs.axis_info[:2]):
            raise ValueError('Topology CRS must be projected with metre units')
        polygons = projected.loc[projected.geom_type.isin(['Polygon', 'MultiPolygon'])]
        overlaps = []
        for i, geom in polygons.geometry.items():
            for j in polygons.sindex.query(geom, predicate='intersects'):
                other = polygons.index[j]
                if other <= i:
                    continue
                area = geom.intersection(polygons.at[other, 'geometry']).area
                if area > 1e-8:
                    overlaps.append({'row_a': int(i), 'row_b': int(other), 'area_m2': float(area)})
                    issue(i, 'POLYGON_OVERLAP', f'row {other}; {area:.3f} m2')
        coverage = union_all(polygons.geometry.to_numpy())
        topology = {'checked': True, 'area_crs': str(projected.crs), 'overlaps': overlaps,
                    'coverage_area_m2': float(coverage.area), 'gap_area_m2': None}
        if boundary is not None:
            if boundary.crs is None or not boundary.geometry.is_valid.all():
                raise ValueError('Boundary must have a CRS and valid geometry')
            target = union_all(boundary.to_crs(area_crs).geometry.to_numpy())
            topology['gap_area_m2'] = float(target.difference(coverage).area)
            topology['outside_boundary_area_m2'] = float(coverage.difference(target).area)
    table = pd.DataFrame(issues, columns=['row', 'code', 'detail'])
    summary = {'features': len(gdf), 'crs': str(gdf.crs) if gdf.crs else None,
               'issue_counts': table.code.value_counts().to_dict(), 'topology': topology,
               'status': 'REVIEW' if len(table) or (topology.get('gap_area_m2') or 0) > 1e-8
               or (topology.get('outside_boundary_area_m2') or 0) > 1e-8 else 'PASS'}
    return summary, table


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input', type=Path)
    p.add_argument('--out-dir', type=Path, default=Path('outputs'))
    p.add_argument('--required-fields', nargs='*', default=[])
    p.add_argument('--class-field')
    p.add_argument('--allowed-classes', nargs='*', default=[])
    p.add_argument('--boundary', type=Path)
    p.add_argument('--area-crs', help='Explicit projected CRS in metres, e.g. EPSG:32645')
    args = p.parse_args()
    boundary = gpd.read_file(args.boundary) if args.boundary else None
    summary, issues = validate(gpd.read_file(args.input), args.required_fields, args.class_field,
                               args.allowed_classes, boundary, args.area_crs)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    (args.out_dir / 'qa_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    issues.to_csv(args.out_dir / 'feature_issues.csv', index=False)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
