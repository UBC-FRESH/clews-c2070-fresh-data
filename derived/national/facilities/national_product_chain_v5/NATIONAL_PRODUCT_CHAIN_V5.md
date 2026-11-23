# National Product Chain V5 (E1 Measured + E2c Density-Calibrated)

Version 4 replaces the nine donor provincial product coefficients with E2c density-calibrated open-data coefficients and adds CFS branch/foliage to their harvest residue. BC, QC, NB and YT keep the E1 measured coefficients.

All values are model estimates: `observed=false`, `policy_grade=false`, `national_claim=false`.

## E1 measured and E2c density-calibrated coefficients

BC/QC/NB/YT keep measured bucking-pilot product shares and total residue. The other nine provinces use E2c density-calibrated open-data coefficients; no donor provincial product share is used.

| Province | Tier | Solid | Pulp | Other | Stem ODT/m3 | Branch+foliage ODT/m3 | Total ODT/m3 |
|---|---|---:|---:|---:|---:|---:|---:|
| BC | measured_bucking_pilot | 0.6953 | 0.2948 | 0.0100 | 0.040577 | 0.121045 | 0.161622 |
| AB | E2c_open_inventory_density_calibrated | 0.4077 | 0.5846 | 0.0077 | 0.014555 | 0.145210 | 0.159765 |
| SK | E2c_open_inventory_density_calibrated | 0.0000 | 0.6432 | 0.3568 | 0.349895 | 0.285004 | 0.634899 |
| MB | E2c_open_inventory_density_calibrated | 0.3919 | 0.5785 | 0.0296 | 0.084668 | 0.109293 | 0.193961 |
| ON | E2c_open_inventory_density_calibrated | 0.4529 | 0.5076 | 0.0396 | 0.084967 | 0.125217 | 0.210184 |
| QC | measured_bucking_pilot | 0.3420 | 0.6417 | 0.0164 | 0.059410 | 0.158097 | 0.217507 |
| NB | measured_bucking_pilot | 0.5238 | 0.4672 | 0.0090 | 0.030341 | 0.157085 | 0.187426 |
| NS | E2c_open_inventory_density_calibrated | 0.2165 | 0.7695 | 0.0140 | 0.123222 | 0.173239 | 0.296461 |
| PE | E2c_open_inventory_density_calibrated | 0.2539 | 0.7274 | 0.0188 | 0.064730 | 0.173242 | 0.237971 |
| NL | E2c_open_inventory_density_calibrated | 0.5103 | 0.4873 | 0.0024 | 0.065918 | 0.154253 | 0.220171 |
| YT | measured_bucking_pilot | 0.4246 | 0.5625 | 0.0129 | 0.123046 | 0.146642 | 0.269689 |
| NT | E2c_open_inventory_density_calibrated | 0.6242 | 0.3589 | 0.0169 | 0.072550 | 0.104472 | 0.177021 |
| NU | E2c_open_inventory_density_calibrated | 0.7051 | 0.2816 | 0.0132 | 0.139130 | 0.137916 | 0.277046 |

## Donor to E2 coefficient change, nine imputed provinces

| Province | Coefficient | Donor | E2 | Delta | E2/donor |
|---|---|---:|---:|---:|---:|
| AB | solid_share | 0.919580 | 0.407699 | -0.511881 | 0.443 |
| AB | pulp_share | 0.000324 | 0.584588 | +0.584263 | 1802.015 |
| AB | other_share | 0.080095 | 0.007714 | -0.072382 | 0.096 |
| AB | total_residue_odt_per_m3 | 0.076226 | 0.159765 | +0.083540 | 2.096 |
| SK | solid_share | 0.919580 | 0.000000 | -0.919580 | 0.000 |
| SK | pulp_share | 0.000324 | 0.643244 | +0.642919 | 1982.824 |
| SK | other_share | 0.080095 | 0.356756 | +0.276661 | 4.454 |
| SK | total_residue_odt_per_m3 | 0.076226 | 0.634899 | +0.558674 | 8.329 |
| MB | solid_share | 0.919580 | 0.391947 | -0.527633 | 0.426 |
| MB | pulp_share | 0.000324 | 0.578453 | +0.578129 | 1783.105 |
| MB | other_share | 0.080095 | 0.029600 | -0.050495 | 0.370 |
| MB | total_residue_odt_per_m3 | 0.076226 | 0.193961 | +0.117735 | 2.545 |
| ON | solid_share | 0.919580 | 0.452861 | -0.466719 | 0.492 |
| ON | pulp_share | 0.000324 | 0.507586 | +0.507262 | 1564.654 |
| ON | other_share | 0.080095 | 0.039553 | -0.040542 | 0.494 |
| ON | total_residue_odt_per_m3 | 0.076226 | 0.210184 | +0.133958 | 2.757 |
| NS | solid_share | 0.919580 | 0.216469 | -0.703112 | 0.235 |
| NS | pulp_share | 0.000324 | 0.769533 | +0.769208 | 2372.115 |
| NS | other_share | 0.080095 | 0.013999 | -0.066097 | 0.175 |
| NS | total_residue_odt_per_m3 | 0.076226 | 0.296461 | +0.220235 | 3.889 |
| PE | solid_share | 0.919580 | 0.253876 | -0.665704 | 0.276 |
| PE | pulp_share | 0.000324 | 0.727352 | +0.727028 | 2242.093 |
| PE | other_share | 0.080095 | 0.018771 | -0.061324 | 0.234 |
| PE | total_residue_odt_per_m3 | 0.076226 | 0.237971 | +0.161746 | 3.122 |
| NL | solid_share | 0.919580 | 0.510307 | -0.409274 | 0.555 |
| NL | pulp_share | 0.000324 | 0.487250 | +0.486926 | 1501.968 |
| NL | other_share | 0.080095 | 0.002443 | -0.077652 | 0.031 |
| NL | total_residue_odt_per_m3 | 0.076226 | 0.220171 | +0.143946 | 2.888 |
| NT | solid_share | 0.919580 | 0.624160 | -0.295421 | 0.679 |
| NT | pulp_share | 0.000324 | 0.358916 | +0.358591 | 1106.372 |
| NT | other_share | 0.080095 | 0.016925 | -0.063171 | 0.211 |
| NT | total_residue_odt_per_m3 | 0.076226 | 0.177021 | +0.100796 | 2.322 |
| NU | solid_share | 0.000000 | 0.705144 | +0.705144 | 0.000 |
| NU | pulp_share | 0.000000 | 0.281628 | +0.281628 | 0.000 |
| NU | other_share | 0.000000 | 0.013227 | +0.013227 | 0.000 |
| NU | total_residue_odt_per_m3 | 0.000000 | 0.277046 | +0.277046 | 0.000 |

## National totals, 119 Mm3 reference harvest

| Metric | Value |
|---|---:|
| harvest_m3 | 118,977,339.100000 |
| sawlog_product_m3 | 33,956,989.460007 |
| pulp_product_odt | 12,066,311.269552 |
| panel_product_m3 | 3,716,637.301052 |
| pellet_product_odt | 5,229,686.166841 |
| bio_product_mwh | 930,946.020335 |
| process_residue_odt | 26,959,509.022730 |
| harvest_residue_gross_odt | 24,022,203.571706 |
| harvest_residue_recoverable_odt | 14,413,322.143037 |
| total_residue_gross_odt | 50,981,712.594426 |
| total_residue_recoverable_odt | 41,372,831.165748 |

Within-class SAW/PANEL and PELLET/BIO splits and mill conversion ratios remain documented donor assumptions. Branch and foliage are dry mass and are never added to stem taper volume.

Labels: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`.

## E2c density calibration and open-volume check

| Province | Density stems/ha | Evidence | Expanded m3/ha | Open m3/ha | Ratio | Status |
|---|---:|---|---:|---:|---:|---|
| AB | 1000.00 | proxy | 409.088 | — | — | not_available |
| SK | 2033.65 | open_inventory | 88.692 | 100.126 | 0.8858 | within_50pct |
| MB | 2050.00 | donor | 251.565 | — | — | not_available |
| ON | 1000.00 | proxy | 122.913 | — | — | not_available |
| NS | 1409.82 | open_inventory | 152.342 | 105.239 | 1.4476 | within_50pct |
| PE | 802.84 | open_inventory | 116.794 | 170.824 | 0.6837 | within_50pct |
| NL | 1000.00 | proxy | 178.398 | — | — | not_available |
| NT | 1000.00 | proxy | 146.149 | — | — | not_available |
| NU | 1000.00 | proxy | 102.728 | — | — | not_available |

## v3.2 versus v4 at fixed harvest

The frozen v3.2 chain uses E2 v1 product coefficients, not E2 v2. The v4 chain replaces them with E2c v3, so the deltas in `v3_2_vs_v4_comparison.csv` are E2 v1 to E2c coefficient effects at fixed assignment and harvest. E2 v2 and E2c share the same per-m3 coefficients; `e2_v2_vs_e2c_coefficients.csv` shows that density calibration is an extensive change (stems/ha and expanded reference volume), not an intensive coefficient change.
