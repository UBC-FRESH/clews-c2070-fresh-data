# FVSCA calibration v0 — QA

Built: 2026-11-14T21:51:57Z
Code: `90695aafe9286721fe11a932d5f71229684822d9`

## Source reconciliation

Input counts are the selected source rows after the optional `--max-sites` filter. `delta` is `(out - in) / in`.

| source | sites in | sites out | visits in | visits out | trees in | trees out | intervals | delta sites | delta visits | delta trees |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| faib_psp | 7341 | 7341 | 23956 | 23956 | 3217648 | 3217643 | 1799382 | 0.0000% | 0.0000% | -0.0002% |
| faib_non_psp | 9512 | 9512 | 11951 | 11951 | 367096 | 366788 | 80702 | 0.0000% | 0.0000% | -0.0839% |
| magplot | 39130 | 39130 | 257031 | 257031 | 7771041 | 7771041 | 3293792 | 0.0000% | 0.0000% | 0.0000% |
| magplot_wfs | 2778 | 2778 | 13906 | 13906 | 1309173 | 1298474 | 369878 | 0.0000% | 0.0000% | -0.8172% |
| qc_pep | 12834 | 12834 | 53632 | 53632 | 2210417 | 2210417 | 979461 | 0.0000% | 0.0000% | 0.0000% |
| nl_fal | 1380 | 1380 | 7657 | 7657 | 775480 | 775477 | 488111 | 0.0000% | 0.0000% | -0.0004% |

## Dropped rows and reasons

- **faib_psp**: `tree_missing_site_or_tree_key` 5
- **faib_non_psp**: `tree_missing_site_or_tree_key` 308
- **magplot_wfs**: `tree_duplicate_key` 10,699
- **nl_fal**: `tree_duplicate_key` 3, `tree_height_99_sentinel` 1, `tree_site_not_found` 168, `visit_site_not_found` 2

## Unit and domain checks

| source | DBH min | DBH max | height min | height max | years | interval min | interval max |
|---|---:|---:|---:|---:|---|---:|---:|
| faib_psp | 0.5 | 401.7 | 0.37 | 73.3 | 1921.0–2025.0 | 2.0 | 35.0 |
| faib_non_psp | 0.1 | 450.0 | 0.0 | 74.5 | 1995.0–2025.0 | 2.0 | 23.0 |
| magplot | 0.1 | 450.0 | 0.1 | 74.5 | 1921.0–2024.0 | 2.0 | 35.0 |
| magplot_wfs | 0.0 | 133.2 | 0.01 | 46.5 | 1949.0–2019.0 | 2.0 | 38.0 |
| qc_pep | 0.0 | 108.9 | 0.0 | 41.5 | 1970.0–2025.0 | 2.0 | 34.0 |
| nl_fal | 0.0 | 99.0 | 0.0 | 81.0 | 1985.0–2026.0 | 2.0 | 13.0 |

## Site index and age coverage

| source | visits | site index visits | % | age visits | % |
|---|---:|---:|---:|---:|---:|
| faib_psp | 23,956 | 21,639 | 90.3% | 21,976 | 91.7% |
| faib_non_psp | 11,951 | 9,318 | 78.0% | 11,286 | 94.4% |
| magplot | 257,031 | 0 | 0.0% | 0 | 0.0% |
| magplot_wfs | 13,906 | 0 | 0.0% | 0 | 0.0% |
| qc_pep | 53,632 | 0 | 0.0% | 45,816 | 85.4% |
| nl_fal | 7,657 | 0 | 0.0% | 0 | 0.0% |

## Coverage (province × source)

| province | source | sites | remeasured sites | visits | first year | last year | intervals | trees |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BC | faib_non_psp | 9512 | 2028 | 11951 | 1995 | 2025 | 80702 | 366788 |
| BC | faib_psp | 7341 | 5735 | 23956 | 1921 | 2025 | 1799382 | 3217643 |
| BC | magplot | 16517 | 13338 | 58902 | 1921 | 2023 | 1872205 | 3830172 |
| MB | magplot | 2 | 2 | 4 | 2024 | 2024 | 0 | 43 |
| NB | magplot | 7609 | 6948 | 14877 | 2016 | 2023 | 12438 | 564150 |
| NL | magplot | 1350 | 1179 | 7093 | 1985 | 2023 | 437093 | 649459 |
| NL | magplot_wfs | 39 | 37 | 113 | 1986 | 2019 | 6244 | 10699 |
| NL | nl_fal | 1380 | 1241 | 7657 | 1985 | 2026 | 488111 | 775477 |
| NT | magplot | 262 | 233 | 495 | 2023 | 2024 | 0 | 14471 |
| PE | magplot_wfs | 691 | 684 | 5290 | 1976 | 2018 | 216689 | 275204 |
| QC | magplot | 12892 | 12851 | 172901 | 1970 | 2024 | 919012 | 2596029 |
| QC | qc_pep | 12834 | 12611 | 53632 | 1970 | 2025 | 979461 | 2210417 |
| SK | magplot | 171 | 149 | 320 | 2024 | 2024 | 0 | 10054 |
| SK | magplot_wfs | 2048 | 1673 | 8503 | 1949 | 2019 | 146945 | 1012571 |
| YT | magplot | 327 | 322 | 2439 | 1988 | 2024 | 53044 | 106663 |

## Known issues

- faib_psp: visit_id is CLSTR_ID; a site may contain several plots but the visit table is site-level.
- faib_psp: site_index is the maximum of the compiled species-level SI columns for the visit; age is the maximum compiled total age. A small number of compiled ages exceed 1000 years and are retained as source values.
- faib_psp: 5 tree rows with a blank PLOT/TREE_NO were dropped.
- faib_non_psp: visit_id is CLSTR_ID; a site may contain several plots but the visit table is site-level.
- faib_non_psp: site_index is the maximum of the compiled species-level SI columns for the visit; age is the maximum compiled total age. A small number of compiled ages exceed 1000 years and are retained as source values.
- faib_non_psp: 308 tree rows with a blank PLOT/TREE_NO were dropped.
- magplot: visit_id is plot_id|meas_num; nested large/small/regeneration plots are kept separate to avoid double counting.
- magplot_wfs: WFS-only sites are those absent from the ZIP package; 39,062 ZIP-overlapping sites and 590,919 overlapping tree features are excluded to avoid double counting.
- magplot_wfs: The NL WFS tree layers 0_2 and 3_9 repeat the same 10,699 tree features for the 39 WFS-only NL sites; exact duplicate keys are dropped.
- qc_pep: eco_zone is classi_eco_pe.reg_eco; eco_subzone is the visit-level station_pe.type_eco mode. No numeric site index is stored.
- qc_pep: plot_area_ha is derived as 10000/median(tige_ha) after tree load; no BAF is present because plots are fixed-area.
- nl_fal: visit year from remeasurement_crew_date.ORIGINAL_DATE, not from the REMEASUREMENT sequence number.
- nl_fal: PLOTSIZE is interpreted as square metres (source has no coded domain); no per-tree expansion factor is available, so BA/TPH are null.
- nl_fal: TREEHEIGHT=99 is the documented sentinel; those values are null. No source expansion factor is present.
- nl_fal: Three exact duplicate tree records (same PLOTKEY/REMEASUREMENT/TREENUMBER) were dropped; 168 tallies did not match a site-layer PLOTKEY and were dropped.
- nl_fal: Two remeasurement visits belong to PLOTKEY 8_119019, which is absent from the point layers; they and its 168 tallies are dropped.


## Validation

52 checks, 0 failed.

| check | status | detail |
|---|---|---|
| site columns | PASS | 18 columns |
| visit columns | PASS | 12 columns |
| tree columns | PASS | 13 columns |
| interval columns | PASS | 12 columns |
| no duplicate sites key | PASS | 0 duplicate rows |
| no duplicate visits key | PASS | 0 duplicate rows |
| no duplicate trees key | PASS | 0 duplicate rows |
| no duplicate intervals key | PASS | 0 duplicate rows |
| visit site referential integrity | PASS | 0 of 72,748 distinct keys have no match |
| tree visit referential integrity | PASS | 0 of 357,300 distinct keys have no match |
| interval tree referential integrity | PASS | 0 of 3,169,855 distinct keys have no match |
| site keys complete | PASS | null source/site_id |
| visit keys complete | PASS | null source/site_id/visit_id |
| tree keys complete | PASS | null source/site_id/visit_id/tree_id |
| DBH range | PASS | observed [0.0, 450.0] cm |
| height range | PASS | observed [0.0, 81.0] m |
| tree status domain | PASS | values ['dead', 'live', 'missing'] |
| species group domain | PASS | values ['conifer', 'deciduous', 'unknown'] |
| visit year range | PASS | observed [1921, 2026] |
| interval length | PASS | observed [2, 38] years |
| interval year range | PASS | year0 [1921, 2022], year1 [1925, 2026] |
| interval arithmetic | PASS | years must equal year1-year0 |
| interval exposure | PASS | exposure_years must equal years*known |
| interval end status | PASS | values ['dead', 'live'] |
| interval flags | PASS | dead/known must be 0/1 and dead must match status_end |
| site n_visits consistency | PASS | 0 of 72,975 site keys disagree |
| site n_trees consistency | PASS | 0 of 72,975 site keys disagree |
| visit n_trees consistency | PASS | 0 of 368,133 site keys disagree |
| faib_psp manifest counts | PASS | all four tables match |
| faib_psp sites reconciliation | PASS | 0.0000% difference; dropped reasons: tree_missing_site_or_tree_key |
| faib_psp visits reconciliation | PASS | 0.0000% difference; dropped reasons: tree_missing_site_or_tree_key |
| faib_psp trees reconciliation | PASS | 0.0002% difference; dropped reasons: tree_missing_site_or_tree_key |
| faib_non_psp manifest counts | PASS | all four tables match |
| faib_non_psp sites reconciliation | PASS | 0.0000% difference; dropped reasons: tree_missing_site_or_tree_key |
| faib_non_psp visits reconciliation | PASS | 0.0000% difference; dropped reasons: tree_missing_site_or_tree_key |
| faib_non_psp trees reconciliation | PASS | 0.0839% difference; dropped reasons: tree_missing_site_or_tree_key |
| magplot manifest counts | PASS | all four tables match |
| magplot sites reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| magplot visits reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| magplot trees reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| magplot_wfs manifest counts | PASS | all four tables match |
| magplot_wfs sites reconciliation | PASS | 0.0000% difference; dropped reasons: tree_duplicate_key |
| magplot_wfs visits reconciliation | PASS | 0.0000% difference; dropped reasons: tree_duplicate_key |
| magplot_wfs trees reconciliation | PASS | 0.8172% difference; dropped reasons: tree_duplicate_key |
| qc_pep manifest counts | PASS | all four tables match |
| qc_pep sites reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| qc_pep visits reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| qc_pep trees reconciliation | PASS | 0.0000% difference; dropped reasons: none |
| nl_fal manifest counts | PASS | all four tables match |
| nl_fal sites reconciliation | PASS | 0.0000% difference; dropped reasons: tree_duplicate_key, tree_height_99_sentinel, tree_site_not_found, visit_site_not_found |
| nl_fal visits reconciliation | PASS | 0.0000% difference; dropped reasons: tree_duplicate_key, tree_height_99_sentinel, tree_site_not_found, visit_site_not_found |
| nl_fal trees reconciliation | PASS | 0.0004% difference; dropped reasons: tree_duplicate_key, tree_height_99_sentinel, tree_site_not_found, visit_site_not_found |

