# National RSYC residue factors and harvest sensitivity

Status: **derived / provisional**. Built from the completed area-weighted
national representative-stand batch. This is not an annual national supply
forecast and not a production-calibrated fuel offer.

Generated: 2026-11-18T17:54:55+00:00

## 1. Definition and headline factor

The residue stream is the **bucking / taper residue** in the national batch:
the non-merchantable portion of the stem after sawlog, pulpwood, and other
product sorts are removed. It is not full aboveground slash (no branches,
bark, or foliage). Recovery is a **roadside recovery** fraction applied to
that gross taper residue. Energy uses **18.5 GJ/ODT** dry LHV and
**1 PJ = 1,000,000 GJ**. The base variable cost is **$2.456978/GJ**; the low
and high cases apply multipliers 1.30 and 0.80.

| National batch quantity | Value |
|---|---:|
| Log volume (m3) | 42,159,162,914.456 |
| Residue volume (m3) | 13,115,814,989.168 |
| Residue ODT | 4,925,060,250.174 |
| Gross residue factor (ODT/m3 log) | 0.116820637 |
| Effective residue density (ODT/m3) | 0.375505468 |
| Area emitted (ha) | 419,793,451.316 |

| Metric | Gross | Low (0.35) | Base (0.60) | High (0.75) |
|---|---:|---:|---:|---:|
| ODT per m3 log | 0.116820637 | 0.040887223 | 0.070092382 | 0.087615477 |
| PJ per million m3 log | 2.161182 | 0.756414 | 1.296709 | 1.620886 |
| PJ per 100 million m3 log | 216.118178 | 75.641362 | 129.670907 | 162.088633 |

The batch log total is a **standing stock** over the emitted area, not an
annual harvest. Do not divide it by a rotation length and call it supply.
The factor above is the deliverable; the harvest table applies it to
explicit annual harvest levels.

## 2. By province

Province values are a **species-resolved SCANFI area-share apportionment** of
the ecoprovince batch cells. The batch itself emits only at the ecoprovince
level; there is no province column in `national_assortment_matrix.csv`. Each
cell is allocated to provinces by the area of that cell's species inside the
ecoprovince, using `national_area_weights_ecodistrict.csv`. The allocation
conserves national log, residue ODT, and emitted area exactly. It does not
create province-specific taper or bucking behaviour; the ecoprovince factor is
applied uniformly within the ecoprovince. Province coverage can differ from
100% by less than 1e-8 because the species area weights and the province
forest-area totals are independently rounded; this is not a land-base
expansion.

| Province | Log (Gm3) | Residue (M ODT) | ODT/m3 | Rec. ODT/m3 low | base | high | PJ/Mm3 base | Area (Mha) | Coverage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AB | 5.304 | 522.198 | 0.098460765 | 0.034461268 | 0.059076459 | 0.073845574 | 1.092914 | 38.346 | 100.000% |
| BC | 12.432 | 1242.296 | 0.099930099 | 0.034975534 | 0.059958059 | 0.074947574 | 1.109224 | 66.602 | 99.991% |
| MB | 2.086 | 397.051 | 0.190324248 | 0.066613487 | 0.114194549 | 0.142743186 | 2.112599 | 33.753 | 99.998% |
| NB | 0.889 | 56.839 | 0.063957219 | 0.022385026 | 0.038374331 | 0.047967914 | 0.709925 | 6.692 | 100.000% |
| NL | 0.925 | 317.087 | 0.342910232 | 0.120018581 | 0.205746139 | 0.257182674 | 3.806304 | 22.883 | 97.242% |
| NS | 0.584 | 39.862 | 0.068299302 | 0.023904756 | 0.040979581 | 0.051224477 | 0.758122 | 4.728 | 100.000% |
| NT | 1.967 | 497.268 | 0.252847783 | 0.088496724 | 0.151708670 | 0.189635837 | 2.806610 | 41.479 | 95.441% |
| NU | 0.082 | 22.929 | 0.280980007 | 0.098343002 | 0.168588004 | 0.210735005 | 3.118878 | 2.834 | 100.000% |
| ON | 6.618 | 611.228 | 0.092354102 | 0.032323936 | 0.055412461 | 0.069265577 | 1.025131 | 68.479 | 99.945% |
| PE | 0.024 | 3.235 | 0.137148837 | 0.048002093 | 0.082289302 | 0.102861628 | 1.522352 | 0.274 | 100.000% |
| QC | 7.548 | 625.624 | 0.082889200 | 0.029011220 | 0.049733520 | 0.062166900 | 0.920070 | 81.662 | 99.999% |
| SK | 1.921 | 336.296 | 0.175042880 | 0.061265008 | 0.105025728 | 0.131282160 | 1.942976 | 26.161 | 100.000% |
| YT | 1.782 | 253.148 | 0.142091736 | 0.049732108 | 0.085255042 | 0.106568802 | 1.577218 | 25.899 | 99.974% |

The full machine-readable table is `residue_factor_by_province.csv`.

## 3. By ecoprovince

`residue_factor_by_ecoprovince.csv` has all 36
emitted ecoprovinces. The factors span a wide range because species and taper
geometry differ. Lowest and highest values:

| Ecoprovince | ODT/m3 | PJ/Mm3 base | Log (Gm3) |
|---|---:|---:|---:|
| Northern Coastal Mountains | 0.012241897 | 0.135885 | 0.116 |
| Georgia Depression | 0.015229214 | 0.169044 | 0.594 |
| Southern Boreal Shield | 0.021021865 | 0.233343 | 5.214 |
| Columbia Montane Cordillera | 0.022688675 | 0.251844 | 3.436 |
| Hudson-James Lowlands | 0.487033978 | 5.406077 | 0.388 |
| Hudson Bay Coastal Plains | 0.589488305 | 6.543320 | 0.039 |
| Newfoundland | 0.935832569 | 10.387742 | 0.144 |
| Northern Montane Cordillera | 0.997409066 | 11.071241 | 0.609 |

The national factor is the log-volume-weighted rollup of these ecoprovince
factors. It is not an unweighted average. The full table also reports area
emitted, forest area, and coverage for each ecoprovince.

## 4. Harvest sensitivity

The table is linear in harvest volume: residue ODT = national factor x log
volume x recovery. It does not model a supply curve, cost escalation, or
changes in harvest mix. It is a sensitivity envelope, not a forecast.

| Harvest (Mm3/y) | Case | Recovery | Gross ODT (M/y) | Recoverable ODT (M/y) | PJ/y | Cost ($/GJ) | x 50 PJ | x 43.524 PJ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 | low | 0.350000 | 11.682 | 4.089 | 75.641362 | 3.194071 | 1.512827 | 1.737930 |
| 100 | base | 0.600000 | 11.682 | 7.009 | 129.670907 | 2.456978 | 2.593418 | 2.979309 |
| 100 | high | 0.750000 | 11.682 | 8.762 | 162.088633 | 1.965582 | 3.241773 | 3.724137 |
| 150 | low | 0.350000 | 17.523 | 6.133 | 113.462043 | 3.194071 | 2.269241 | 2.606896 |
| 150 | base | 0.600000 | 17.523 | 10.514 | 194.506360 | 2.456978 | 3.890127 | 4.468964 |
| 150 | high | 0.750000 | 17.523 | 13.142 | 243.132950 | 1.965582 | 4.862659 | 5.586205 |
| 200 | low | 0.350000 | 23.364 | 8.177 | 151.282724 | 3.194071 | 3.025654 | 3.475861 |
| 200 | base | 0.600000 | 23.364 | 14.018 | 259.341813 | 2.456978 | 5.186836 | 5.958618 |
| 200 | high | 0.750000 | 23.364 | 17.523 | 324.177267 | 1.965582 | 6.483545 | 7.448273 |
| 250 | low | 0.350000 | 29.205 | 10.222 | 189.103405 | 3.194071 | 3.782068 | 4.344826 |
| 250 | base | 0.600000 | 29.205 | 17.523 | 324.177267 | 2.456978 | 6.483545 | 7.448273 |
| 250 | high | 0.750000 | 29.205 | 21.904 | 405.221583 | 1.965582 | 8.104432 | 9.310341 |

Comparison anchors:

- **50.000 PJ**: task-stated current C2070 `SUPBCW` placeholder.
- **43.523816 PJ**: BC-only base cap in 2028-2070 from
  `BC_RESIDUE_RECOVERY_REPORT.md`.
- Current `SUPBCW_activity_limits_base.csv`: 50.325738 PJ in
  2021, 43.523816 PJ in
  2070.

At 100 million m3/yr the base case is **129.670907 PJ/yr**,
which is **2.593x** the 50 PJ placeholder
and **2.979x** the BC-only 43.523816 PJ cap.
Even the low case at 100 million m3/yr (75.641 PJ) is above
both anchors. The comparison is a scale comparison, not like-for-like: the
43.523816 PJ BC cap is set on a 43.370776 million m3/yr 2028-2070
harvest, whereas the national rows are 100-250 million m3/yr. The 2021 BC cap
of 50.325738 PJ uses the 52.774801 million m3/yr 2021 AAC.

A scale-normalized comparison puts the BC-only base at
**100.352865 PJ per 100 million m3** of log. The national base factor
is **129.670907 PJ per 100 million m3**, or
**1.292x** the BC factor. The difference is
documented, not reconciled: the national batch is area-weighted across all
forest land, while the BC chain is a BC harvest-weighted AAC calculation, and
the batch definitions/area joins differ.

## 5. Reference harvest basis: decision flag

**No documented national annual harvest level was found in the repository.**
`planning/national-rsyc-backbone.md` (gap G1) states that RSYC gives m3/ha by
age, not a harvest level, and that a national AAC/harvest scenario and
annualization rule must be adopted before a national supply total can be
published. The only documented annual harvest in this chain is the BC AAC
(52,774,801 m3/yr in 2018; 43,370,776 m3/yr in 2028-2070), which is
provincial and is used only for the BC comparison.

Therefore:

- the 100/150/200/250 million m3/yr rows are a **range**, not a recommendation;
- no reference harvest is selected here;
- selecting a national harvest basis remains an explicit decision.

If a harvest allocation by province or ecoprovince becomes available, apply
the provincial/ecoprovincial factors in this directory to that allocation
instead of applying the single national factor. A harvest-weighted mix is
likely to differ from the area-weighted standing mix and would move the
residue factor.

## 6. Validation, coverage, and failed cells

| Check | Status | Value | Note |
|---|---:|---:|---:|
| residue_odt_equals_volume_times_density | PASS | max cell relative error < 1e-9 | checked per residue row and per cell |
| log_plus_residue_equals_total | PASS | max cell relative error < 1e-9 | checked for every emitted cell |
| no_nan_or_negative | PASS | 265 cells checked | all matrix numeric fields finite and non-negative |
| stand_area_and_density_crosscheck | PASS | max area rel 0.000e+00; max density rel 0.000e+00 | national_stands.csv matches matrix cells |
| batch_summary_area_reconciliation | PASS | summary emitted 419793451.316; mapped 422475761.522 | national_assortment_summary.json area reconciliation matches this builder |
| province_sums_equal_national_log | PASS | 42159162914.456 vs 42159162914.456 | species-resolved SCANFI area-share allocation |
| province_sums_equal_national_residue_odt | PASS | 4925060250.174 vs 4925060250.174 | same allocation |
| province_sums_equal_national_area | PASS | 419793451.316 vs 419793451.316 | same allocation |
| ecoprovince_sums_equal_national | PASS | log 42159162914.456; ODT 4925060250.174; area 419793451.316 | direct ecoprovince rollup |
| species_province_allocation_area_match | PASS | max rel 2.143e-15 | each cell area equals the sum of its species x province weights |
| area_coverage_vs_mapped_forest | INFO | emitted 419.793451 Mha / mapped 422.475761 Mha = 0.993650974 | gap 2.682310 Mha = 0.006349 fraction |
| area_base_crosscheck | INFO | ecodistrict sum 422475761.070 ha; area-join mapped 422475761.522 ha | difference -0.452 ha; negligible aggregation rounding, not a missing cell |
| failed_cell_documented | INFO | ecoprovince:Taiga Plains/Great Bear Lowlands\|PINU.BAN at 1.987823 Mha | status=failed; excluded from emitted area and totals |
| zero_log_cell | INFO | 1 cell(s): ecoprovince:Boreal Shield East/Newfoundland\|PINU.BAN | ratio undefined at cell level; national and ecoprovince aggregates have positive log |

Coverage: emitted **419.793451 Mha** (the 419.79M ha batch
figure) against mapped positive SCANFI forest area
**422.475761 Mha**. The gap is
**2.682310 Mha** (**0.6349%**; the reported
0.64% figure). The failed cell alone is **1.987823
Mha**.

Failed cell:

| Field | Value |
|---|---|
| Cell | `ecoprovince:Taiga Plains/Great Bear Lowlands\|PINU.BAN` |
| Ecoprovince | Taiga Plains/Great Bear Lowlands |
| Species | PINU.BAN |
| Status | failed |
| Reason | `(empty)` |
| Flags | `area_scanfi;taper_proxy` |
| Area | 1,987,822.629 ha |

Cell-status accounting:

| Cell status | Cells | Area (Mha) |
|---|---:|---:|
| failed | 1 | 1.987823 |
| ok | 265 | 419.793451 |
| skipped_no_fit | 19 | 0.045537 |
| skipped_no_taper_mapping | 33 | 0.000000 |
| skipped_no_tph | 1 | 0.648951 |
| skipped_unmapped_species_area | 781 | 0.000000 |
| skipped_zero_area | 160 | 0.000000 |

The failed cell is `PINU.BAN` in Great Bear Lowlands. It is excluded from the
emitted matrix and therefore from every total. The remaining gap is dominated
by the `skipped_no_tph` Newfoundland `BROADLEAF` cell (648,950.533 ha) and
`skipped_no_fit` cells (45,537.045 ha total). Unmapped-species and zero-area
cells carry zero positive area.

One emitted cell,
`ecoprovince:Boreal Shield East/Newfoundland|PINU.BAN`, has zero log volume
and 2,478.571 ODT of residue over 0.045 ha. Its cell-level ODT/m3 is
undefined; it is retained in the aggregate because its residue is real, and
it does not make any ecoprovince or national log denominator zero.

## 7. Method, inputs, and caveats

Inputs:

- `/tmp/rsyc_backbone_repo/out/full/national_assortment_matrix.csv` - bucking matrix; log, residue, total, density, area.
- `/tmp/rsyc_backbone_repo/out/full/national_stands.csv` - cell area and density cross-check.
- `/tmp/rsyc_backbone_repo/out/full/national_batch_area_join_full.csv` - declared but missing.
- `/tmp/rsyc_backbone_repo/out/national_batch_area_join_full.csv` - used area join; forest area and cell area.
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/assortments/national_area_weights/national_area_weights_ecodistrict.csv` - species x province allocation weights.
- `/tmp/rsyc_backbone_repo/out/full/cell_status.csv` - status and failed-cell audit.
- `/tmp/rsyc_backbone_repo/out/full/national_assortment_summary.json` - batch area reconciliation cross-check.
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/clews/comparison/SUPBCW_activity_limits_base.csv` - current BC-only parameter comparison.
- `/srv/shared-data/gep/jupyterhub16-projects/clews-c2070-fresh/data/derived/national/clews/bc_residue_time_path.csv` - BC 2028-2070 annual log basis for the normalized comparison.

Input path correction: The declared input path `out/full/national_batch_area_join_full.csv` does not exist. The documented file at `out/national_batch_area_join_full.csv` was used. This is the only input-path substitution; the file contents are the batch area join.

Checks performed: residue ODT = residue m3 x cell density; log + residue =
total; no NaN, infinity, or negative values; national stands area and density
match the matrix; per-province and per-ecoprovince sums equal national;
species x province allocation areas match each cell; area coverage and failed
cell documented. All hard checks pass.

Caveats:

1. The batch is a representative-stand, area-weighted standing-stock
   calculation. It is not an observed harvest census.
2. The residue definition is taper/bucking residue, not full aboveground
   slash. It excludes branches, bark, and foliage.
3. Recovery 0.35/0.60/0.75 is applied uniformly to every ecoprovince. No
   regional recovery evidence is available in this batch.
4. The province split is an area-share apportionment, not a province-specific
   yield or taper model. Only the ecoprovince values are direct batch outputs.
5. Cost is a flat $/GJ proxy with case multipliers. It is not a delivered-cost
   curve and does not vary with harvest level, distance, or scale.
6. The national factor is higher than the BC-only harvest-weighted factor
   because the area-weighted mix includes high-residue boreal and taiga
   ecoprovinces. Do not substitute one for the other without a harvest
   allocation.
7. The area base is gross SCANFI treed area (422.475761 Mha), with no THLB or
   operability filter (`planning/national-rsyc-backbone.md`, gap G2).

## 8. Outputs and status

All outputs are in `data/derived/national/clews_supply/rsyc_backbone/`:

- `residue_factor_by_province.csv`
- `residue_factor_by_ecoprovince.csv`
- `harvest_sensitivity.csv`
- `national_residue_factor_summary.json`
- `province_allocation.csv`
- `validation_checks.csv`
- `manifest.json`
- `NATIONAL_RESIDUE_FACTOR_REPORT.md`

Status: **complete for the requested factor and sensitivity deliverables**.
Not committed. The reference-harvest decision and any THLB/operability filter
remain open.
