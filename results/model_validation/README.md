# Validation of the UrbanMask classifiers

Results of the validation protocols run on this observation base for the deployed PCA + Random Forest model and the HEU rule. All runs used:
- the StandardScaler → PCA (95% variance, 6 components) → Random Forest pipeline, with 100 trees and maximum depth 12;
- seed 42;
- the 4,383,413 unique pixel-years unless stated.

Test names inside the CSV files are in Portuguese; the table maps them.

| File | Protocol | Key result |
|---|---|---|
| `prova0_modelo_implantado.json` | Inspection of the deployed model | 6 PCA components (95.9% variance), 100 trees, depth 12, threshold 0.291; fitted on 10,986,265 rows (random 80% of the raw 13.7 M rows) |
| `prova1_vazamento_2023.csv` | Deployed model on rows seen / not seen in training | Precision 0.51–0.55 and recall 0.62–0.66 in every subset |
| `prova2_temporal.csv` | Train on earlier years, test on the next year (*treino → teste*) | 2020–22 → 2023: precision 0.517 (95% CI 0.513–0.522), recall 0.691 |
| `prova3_espacial.csv` | 5-fold group split on ~3 km blocks (*blocos*); 3b = blocks and year held out together | Mean precision 0.492, recall 0.665; 3b: 0.521 / 0.650 |
| `prova4_heuristica.csv` | HEU rule (4 conditions, production) and a 6-condition variant (*testada*), per year | 2023: 4-condition precision 0.453, recall 0.355 |
| `prova5_limiares.csv`, `prova5_curvas.png` | Optimal threshold per protocol and precision–recall curves | Optimal threshold 0.26–0.31 (deployed 0.291) |
| `prova7_duplicatas.csv` | Random split with (*COM*) and without (*SEM*) duplicated rows | With duplicates: 0.701 / 0.743, 68.4% of test rows copied in training; without: 0.499 / 0.669 |
| `00_amostra_info.json` | Sample description | 13,732,832 raw rows, 9,349,419 duplicates, 4,383,413 unique, 98,684 polygons |

*limiar da validação* = threshold chosen on validation data; *limiar oráculo* = best threshold on the test data (upper bound); *limiar 0,291* = deployed threshold.
