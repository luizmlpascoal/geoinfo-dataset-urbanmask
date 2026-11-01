# APM layer (`apms/apms_goiania.gpkg`)

2,144 municipal public areas (*Áreas Públicas Municipais*, APMs) of Goiânia monitored by UrbanMask. Layer `apms`, MultiPolygon, SIRGAS 2000 (EPSG:4674).

**Provenance.**
- The layer comes from the municipal APM register (Prefeitura de Goiânia, SEPLANH), via the sample layer of the UrbanMask repository (https://github.com/ThiagoHF31/urbanMask).
- Of the 8,428 APMs in the register, 6,430 were selected by the Planning Secretariat. Areas already ceded as plots were then removed, leaving 2,144.
- Fields identifying people were removed: owner name, cadastral/IPTU registration (`ci`, `nr_iptu`, `nr_refiptu`) and check digit. APMs are public land.

| Column | Description |
|---|---|
| `OBJECTID`, `nr_apm`, `cd_geo` | Register identifiers of the APM |
| `cd_log`, `nm_log`, `nr_log` | Street code, street name and number of reference |
| `nm_qdr`, `nm_lot`, `nm_apm`, `compl` | Block, plot, APM label and complement in the subdivision plan |
| `cd_bai`, `nm_bai` | Neighbourhood code and name |
| `cd_destin`, `nm_destin` | Designated purpose in the subdivision plan (e.g. green area, school, square) |
| `cd_grupo_d`, `nm_grupo_d` | Group of the designated purpose |
| `cd_uso`, `nm_uso` | Registered current use (e.g. green area, plot, compromised, invasion) |
| `cd_grupo_u`, `nm_grupo_u` | Use group (used in the paper and in `results/apm_use_groups.csv`; empty for 329 APMs) |
| `area_orig`, `area_atual`, `area_edif` | Original, current and built area recorded in the register (m²) |
| `cd_tipo` | Register type code |

`scripts/apm_analysis.py` rebuilds the 10 m UrbanMask pixel grid on this layer (104,415 pixels) and summarises it by use group (`results/apm_summary.md`).
