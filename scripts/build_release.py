"""Build the public UrbanMask observation base from the raw Earth Engine extraction.

Usage: python scripts/build_release.py <raw_pixels_2020_2023.parquet> data

The raw file (13,732,832 rows, not distributed) repeats pixels shared by touching or
overlapping polygons. For each year this script keeps one row per pixel centre
(lat/lon rounded to 7 decimals), casts the features to float32, adds a ~3 km spatial
block id and writes data/pixels_<year>.parquet (zstd).
"""
import pyarrow.parquet as pq, pyarrow as pa, pandas as pd, numpy as np, json, sys
SRC = sys.argv[1]; OUT = sys.argv[2]
FEAT = ['ndvi','ndvi_re','gndvi','savi','mndwi','ndbi','ui','nbi','bsi','baei','ibi','ndvi_std','entropy','ndbi_std']
summary = {}
for y in [2020, 2021, 2022, 2023]:
    t = pq.read_table(SRC, filters=[('ano', '=', y)])
    d = t.to_pandas(); del t
    n_raw = len(d)
    d['lat_r'] = d['lat'].round(7); d['lon_r'] = d['long'].round(7)
    d = d.drop_duplicates(['lat_r', 'lon_r', 'ano']).copy()
    for c in FEAT:
        d[c] = d[c].replace([np.inf, -np.inf], np.nan).astype('float32')
    out = pd.DataFrame({
        'polygon_id': d['id'].astype('int32'),
        'pixel_id': d['pixel_id'].astype('int64'),
        'year': d['ano'].astype('int16'),
        'lon': d['long'].round(6), 'lat': d['lat'].round(6),
        'block_3km': (np.floor(d['lat'] / 0.03).astype('int32') * 10000 + np.floor(d['long'] / 0.03).astype('int32')).astype('int64'),
    })
    for c in FEAT: out[c] = d[c].values
    out['ob_presence'] = d['google_conf'].astype('float32').values
    out['label_built'] = d['google_target'].fillna(0).astype('int8').values
    out = out.sort_values(['polygon_id', 'pixel_id']).reset_index(drop=True)
    pq.write_table(pa.Table.from_pandas(out, preserve_index=False), f"{OUT}/pixels_{y}.parquet", compression='zstd', compression_level=12)
    summary[y] = dict(rows_raw=int(n_raw), rows_unique=int(len(out)), built=int(out.label_built.sum()),
                      prevalence=round(float(out.label_built.mean()), 4), polygons=int(out.polygon_id.nunique()),
                      nan_rows=int(out[FEAT].isna().any(axis=1).sum()))
    print(y, summary[y], flush=True)
    del d, out
json.dump(summary, open(f"{OUT}/../summary_build.json", 'w'), indent=1)
