# National Representative-Stand Batch (Phase 1)

Generated: 2026-11-17T08:11:18Z  
Runtime: 494.9 s  
Runtime breakdown: prep_seconds 25.3 s, table_seconds 327.6 s, cell_seconds 141.9 s, assemble_seconds 0.2 s  
Status: **pipeline test only**.  Every cell carries a 1 ha placeholder (`area_basis=placeholder_equal_area`); summed totals are not a national supply estimate.

## Design

- Level: `ecoprovince`.
- Cells planned: 1260.
- Stands completed: 1191.
- Buck-yield tables: 488.
- Trees per stand: 300; DBH bins: 2-100 cm at 2 cm.
- Volume target: RSYC volume at age 100; observed plot volume fallback is flagged.
- TPH target: expansion-weighted mean live plot-visit TPH; borrowed cells use the donor level.
- Area: 1 ha placeholder per cell (`placeholder_equal_area`).

### Run status

- `failed`: 3
- `ok`: 1191
- `skipped_no_fit`: 19
- `skipped_no_taper_mapping`: 33
- `skipped_no_tph`: 3
- `synthesis_failed`: 11

### Evidence tiers

- `direct_fit`: 298
- `pooled_fit`: 26
- `pooled_parent`: 122
- `species_national`: 745

### Area and taper proxies

- Area weight is a placeholder, not a mapped national area.
- The taper dispatcher is BC-only.  National species use an explicit published Kozak proxy; every row carries `taper_mapping_basis` and `taper_proxy`.
- BEC zone is an ecozone-level proxy, not a national BEC classification.
- Sorts are dimension-only; `grade_status=not_assigned`.

## Buck-yield table

- Validated cells: 1191 (1184 pass, 7 fail).
- Maximum relative errors: taper 0.05536796919241533, product (material totals) 15.702457736226275, residue 0.34792258641648427.
- Product-total diagnostic: 967 pass, 224 fail.  Product faults are reported, not gated, because a 20-tree sample can straddle a sort threshold.
- Pre-registered tolerances: taper 2% or 0.05 m3; product 5% or 0.02 m3; residue 10% or 0.2 m3.
- Total taper and residue are the gated layer.  Product totals and sort shares are a 2 cm midpoint approximation and are reported as a diagnostic: near a sort threshold a 20-tree sample can move volume between sawlog and pulpwood even when total taper is exact.  Precise product/sort allocation requires per-tree bucking.

## Pilot results

Completed 1191 stands across 1191 cells.  Recovered logs 144415.8 m3, residue 23704.3 m3 (8822.2 ODT), total 168120.1 m3.

### Volume by product

| product | volume m3 | volume m3/ha (equal-area sum) |
|---|---:|---:|
| other | 55674.715 | 55674.715 |
| pulpwood | 1474.952 | 1474.952 |
| sawlog | 87266.150 | 87266.150 |

### Volume and residue by species

| species | volume m3 | residue m3 | residue ODT |
|---|---:|---:|---:|
| ABIE.AMA | 4805.252 | 978.529 | 342.332 |
| ABIE.BAL | 4792.816 | 821.634 | 287.443 |
| ABIE.LAS | 4744.980 | 1262.988 | 391.270 |
| ACER.MAC | 5489.538 | 254.759 | 89.126 |
| ACER.RUB | 5140.933 | 528.481 | 184.885 |
| ACER.SAH | 5795.184 | 576.789 | 201.786 |
| ALNU.RUB | 4806.510 | 903.980 | 316.251 |
| BETU.ALL | 3820.821 | 208.401 | 99.981 |
| BETU.PAP | 4378.978 | 841.259 | 403.597 |
| BROADLEAF | 5340.827 | 538.689 | 188.456 |
| CONIFEROUS | 4802.507 | 629.883 | 226.616 |
| FRAX.NIG | 5450.771 | 301.697 | 105.547 |
| LARI.LAR | 4227.334 | 388.244 | 186.261 |
| LARI.OCC | 4733.971 | 530.860 | 254.682 |
| PICE.ABI | 4810.839 | 1450.272 | 521.772 |
| PICE.ENG | 5439.244 | 618.729 | 204.069 |
| PICE.GLA | 5521.031 | 632.539 | 227.572 |
| PICE.MAR | 4571.666 | 1408.842 | 535.075 |
| PICE.RUB | 4756.967 | 312.520 | 118.695 |
| PICE.SIT | 4817.381 | 395.595 | 130.475 |
| PINU.BAN | 4735.747 | 1028.626 | 390.670 |
| PINU.CON | 4413.326 | 1674.299 | 635.896 |
| PINU.PON | 4192.570 | 279.224 | 106.049 |
| PINU.RES | 4786.187 | 531.663 | 201.925 |
| PINU.STR | 4881.099 | 176.448 | 67.015 |
| POPU.BAL | 5431.922 | 620.625 | 192.268 |
| POPU.GRA | 5294.220 | 350.947 | 122.776 |
| POPU.TRE | 5711.072 | 1138.857 | 398.421 |
| PSEU.MEN | 4948.878 | 863.975 | 388.614 |
| QUER.RUB | 5487.339 | 208.916 | 73.088 |
| THUJ.OCC | 4877.981 | 344.608 | 106.759 |
| THUJ.PLI | 4977.013 | 865.682 | 268.186 |
| TSUG.HET | 6054.837 | 1143.040 | 479.899 |
| TSUG.MER | 4080.333 | 892.654 | 374.776 |

## Conservation and validation

- Maximum synthesis volume relative error: 6.81e-13.
- Maximum synthesis TPH relative error: 4.35e-16.
- Maximum matrix taper vs synthesis taper relative error: 0.0216.
- Matrix recovered log volume + residue = matrix taper total by construction.

## Remaining cells and next stage

- Remaining planned cells without a partial: 0.
- Skipped cells without a synthesis plan: 55.
- Resume with the same command and `--resume` to complete any remaining planned cells.
- Stage A: replace the equal-area placeholder with mapped cell area and a defensible spatial frame before any supply claim.
- Stage B: replace BC taper/sort proxies with jurisdiction-specific taper and grade rules.

