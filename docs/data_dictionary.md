# Data dictionary (`data/pixels_YYYY.parquet`)

One row per Sentinel-2 pixel (10 m) and year. All four files share the same schema.

| Column | Type | Description |
|---|---|---|
| `polygon_id` | int32 | Integer index of the vacant-lot polygon containing the pixel (no cadastral code) |
| `pixel_id` | int64 | Index of the pixel within the extraction batch of its polygon |
| `year` | int16 | Year of the annual composite (2020–2023) |
| `lon`, `lat` | float64 | Pixel-centre coordinates, WGS 84 (EPSG:4326), 6 decimals |
| `block_3km` | int64 | Spatial block of about 3 km (0.03° × 0.03°), for spatially blocked cross-validation |
| `ndvi` | float32 | Normalised difference vegetation index |
| `ndvi_re` | float32 | NDVI with the red-edge band (B5) |
| `gndvi` | float32 | Green NDVI |
| `savi` | float32 | Soil-adjusted vegetation index (L = 0.5) |
| `mndwi` | float32 | Modified normalised difference water index |
| `ndbi` | float32 | Normalised difference built-up index |
| `ui` | float32 | Urban index (SWIR2/NIR normalised difference) |
| `nbi` | float32 | New built-up index (Red × SWIR1 / NIR) |
| `bsi` | float32 | Bare soil index |
| `baei` | float32 | Built-up area extraction index |
| `ibi` | float32 | Index-based built-up index |
| `ndvi_std` | float32 | Standard deviation of NDVI across the valid scenes of the year |
| `entropy` | float32 | GLCM entropy of the NIR band (3 × 3 window) |
| `ndbi_std` | float32 | Standard deviation of NDBI across the valid scenes of the year |
| `ob_presence` | float32 | Open Buildings 2.5D Temporal `building_presence` for the pixel and year (0–1) |
| `label_built` | int8 | 1 if `building_presence ≥ 0.56` and `building_height ≥ 2 m`, else 0 |

Formulas are in [`features.md`](features.md). There are no missing values in the features.
