# Feature formulas and labelling rule

Sentinel-2 Level-2A harmonised surface reflectance (`COPERNICUS/S2_SR_HARMONIZED`); bands renamed as Blue (B2), Green (B3), Red (B4), RE1 (B5), NIR (B8), SWIR1 (B11), SWIR2 (B12) and scaled by 1/10,000.

**Annual composite.**
- Scenes from 1 January to 31 December with `CLOUDY_PIXEL_PERCENTAGE < 20`.
- Clouds and cirrus masked with the QA60 bits; per-pixel median of the valid scenes.

| Feature | Formula (on the annual median unless stated) | Reference |
|---|---|---|
| NDVI | (NIR − Red) / (NIR + Red) | Rouse et al. (1974) |
| NDVI_RE | (NIR − RE1) / (NIR + RE1) | |
| GNDVI | (NIR − Green) / (NIR + Green) | |
| SAVI | 1.5 (NIR − Red) / (NIR + Red + 0.5) | Huete (1988) |
| MNDWI | (Green − SWIR1) / (Green + SWIR1) | Xu (2006) |
| NDBI | (SWIR1 − NIR) / (SWIR1 + NIR) | Zha et al. (2003) |
| UI | (SWIR2 − NIR) / (SWIR2 + NIR) | |
| NBI | Red × SWIR1 / NIR | |
| BSI | ((SWIR1 + Red) − (NIR + Blue)) / ((SWIR1 + Red) + (NIR + Blue)) | |
| BAEI | (Red + 0.3) / (Green + SWIR1) | |
| IBI | (NDBI − (SAVI + MNDWI)/2) / (NDBI + (SAVI + MNDWI)/2) | |
| ndvi_std | standard deviation of per-scene NDVI over the year | |
| ndbi_std | standard deviation of per-scene NDBI over the year | |
| entropy | GLCM entropy of NIR × 10,000 (integer), window size 3 | Haralick et al. (1973) |

**Label.** Open Buildings 2.5D Temporal v1 (`GOOGLE/Research/open-buildings-temporal/v1`) for the same year:

```
label_built = 1  if building_presence >= 0.56 and building_height >= 2 m
              0  otherwise
```

**HEU rule used by UrbanMask** (reproduced in `results/heuristic_by_year.csv`):

```
NBI > 0.18 and UI > 0.05 and NDVI < 0.20 and MNDWI > -0.50
```

Note that IBI has a near-zero denominator for some pixels, which explains its wide range.

## References

- Haralick, R. M., Shanmugam, K. and Dinstein, I. (1973). Textural features for image classification. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-3(6):610–621. doi:10.1109/TSMC.1973.4309314.
- Huete, A. R. (1988). A soil-adjusted vegetation index (SAVI). *Remote Sensing of Environment*, 25(3):295–309. doi:10.1016/0034-4257(88)90106-X.
- Rouse, J. W., Haas, R. H., Schell, J. A. and Deering, D. W. (1974). Monitoring vegetation systems in the Great Plains with ERTS. *NASA Special Publication*, 351:309–317.
- Xu, H. (2006). Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery. *International Journal of Remote Sensing*, 27(14):3025–3033. doi:10.1080/01431160600589179.
- Zha, Y., Gao, J. and Ni, S. (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. *International Journal of Remote Sensing*, 24(3):583–594. doi:10.1080/01431160304987.
