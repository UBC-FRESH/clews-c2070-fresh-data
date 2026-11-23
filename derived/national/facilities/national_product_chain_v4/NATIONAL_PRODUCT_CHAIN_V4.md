# National Product Chain V4 (E1 Measured + E2 Imputed Coefficients)

Version 4 replaces the nine donor provincial product coefficients with E2 open-data imputation coefficients and adds CFS branch/foliage to their harvest residue. BC, QC, NB and YT keep the E1 measured coefficients.

All values are model estimates: `observed=false`, `policy_grade=false`, `national_claim=false`.

## E1 measured and E2 imputed coefficients

BC/QC/NB/YT keep measured bucking-pilot product shares and total residue. The other nine provinces use E2 open-data imputation coefficients; no donor provincial product share is used.

| Province | Tier | Solid | Pulp | Other | Stem ODT/m3 | Branch+foliage ODT/m3 | Total ODT/m3 |
|---|---|---:|---:|---:|---:|---:|---:|
| BC | measured_bucking_pilot | 0.6953 | 0.2948 | 0.0100 | 0.040577 | 0.121045 | 0.161622 |
| AB | e2_open_data_imputation | 0.5985 | 0.3773 | 0.0242 | 0.040511 | 0.092006 | 0.132517 |
| SK | e2_open_data_imputation | 0.4704 | 0.5008 | 0.0288 | 0.063432 | 0.105375 | 0.168808 |
| MB | e2_open_data_imputation | 0.5099 | 0.4611 | 0.0290 | 0.094930 | 0.123141 | 0.218071 |
| ON | e2_open_data_imputation | 0.4529 | 0.5076 | 0.0396 | 0.083483 | 0.124172 | 0.207654 |
| QC | measured_bucking_pilot | 0.3420 | 0.6417 | 0.0164 | 0.059410 | 0.158097 | 0.217507 |
| NB | measured_bucking_pilot | 0.5238 | 0.4672 | 0.0090 | 0.030341 | 0.157085 | 0.187426 |
| NS | e2_open_data_imputation | 0.4080 | 0.5754 | 0.0166 | 0.038670 | 0.154820 | 0.193490 |
| PE | e2_open_data_imputation | 0.3840 | 0.5908 | 0.0252 | 0.034972 | 0.149139 | 0.184111 |
| NL | e2_open_data_imputation | 0.5103 | 0.4873 | 0.0024 | 0.065621 | 0.154070 | 0.219691 |
| YT | measured_bucking_pilot | 0.4246 | 0.5625 | 0.0129 | 0.123046 | 0.146642 | 0.269689 |
| NT | e2_open_data_imputation | 0.6242 | 0.3589 | 0.0169 | 0.070509 | 0.103371 | 0.173880 |
| NU | e2_open_data_imputation | 0.7051 | 0.2816 | 0.0132 | 0.137096 | 0.137126 | 0.274223 |

## Donor to E2 coefficient change, nine imputed provinces

| Province | Coefficient | Donor | E2 | Delta | E2/donor |
|---|---|---:|---:|---:|---:|
| AB | solid_share | 0.919580 | 0.598498 | -0.321083 | 0.651 |
| AB | pulp_share | 0.000324 | 0.377349 | +0.377024 | 1163.192 |
| AB | other_share | 0.080095 | 0.024154 | -0.055942 | 0.302 |
| AB | total_residue_odt_per_m3 | 0.076226 | 0.132517 | +0.056292 | 1.738 |
| SK | solid_share | 0.919580 | 0.470357 | -0.449223 | 0.511 |
| SK | pulp_share | 0.000324 | 0.500807 | +0.500483 | 1543.758 |
| SK | other_share | 0.080095 | 0.028836 | -0.051259 | 0.360 |
| SK | total_residue_odt_per_m3 | 0.076226 | 0.168808 | +0.092582 | 2.215 |
| MB | solid_share | 0.919580 | 0.509861 | -0.409719 | 0.554 |
| MB | pulp_share | 0.000324 | 0.461098 | +0.460774 | 1421.354 |
| MB | other_share | 0.080095 | 0.029040 | -0.051055 | 0.363 |
| MB | total_residue_odt_per_m3 | 0.076226 | 0.218071 | +0.141845 | 2.861 |
| ON | solid_share | 0.919580 | 0.452861 | -0.466719 | 0.492 |
| ON | pulp_share | 0.000324 | 0.507586 | +0.507262 | 1564.654 |
| ON | other_share | 0.080095 | 0.039553 | -0.040542 | 0.494 |
| ON | total_residue_odt_per_m3 | 0.076226 | 0.207654 | +0.131429 | 2.724 |
| NS | solid_share | 0.919580 | 0.408008 | -0.511572 | 0.444 |
| NS | pulp_share | 0.000324 | 0.575437 | +0.575112 | 1773.806 |
| NS | other_share | 0.080095 | 0.016555 | -0.063540 | 0.207 |
| NS | total_residue_odt_per_m3 | 0.076226 | 0.193490 | +0.117265 | 2.538 |
| PE | solid_share | 0.919580 | 0.383975 | -0.535605 | 0.418 |
| PE | pulp_share | 0.000324 | 0.590848 | +0.590523 | 1821.312 |
| PE | other_share | 0.080095 | 0.025177 | -0.054918 | 0.314 |
| PE | total_residue_odt_per_m3 | 0.076226 | 0.184111 | +0.107885 | 2.415 |
| NL | solid_share | 0.919580 | 0.510307 | -0.409274 | 0.555 |
| NL | pulp_share | 0.000324 | 0.487250 | +0.486926 | 1501.968 |
| NL | other_share | 0.080095 | 0.002443 | -0.077652 | 0.031 |
| NL | total_residue_odt_per_m3 | 0.076226 | 0.219691 | +0.143465 | 2.882 |
| NT | solid_share | 0.919580 | 0.624160 | -0.295421 | 0.679 |
| NT | pulp_share | 0.000324 | 0.358916 | +0.358591 | 1106.372 |
| NT | other_share | 0.080095 | 0.016925 | -0.063171 | 0.211 |
| NT | total_residue_odt_per_m3 | 0.076226 | 0.173880 | +0.097655 | 2.281 |
| NU | solid_share | 0.000000 | 0.705144 | +0.705144 | 0.000 |
| NU | pulp_share | 0.000000 | 0.281628 | +0.281628 | 0.000 |
| NU | other_share | 0.000000 | 0.013227 | +0.013227 | 0.000 |
| NU | total_residue_odt_per_m3 | 0.000000 | 0.274223 | +0.274223 | 0.000 |

## National totals, 119 Mm3 reference harvest

| Metric | Value |
|---|---:|
| harvest_m3 | 118,977,339.100000 |
| sawlog_product_m3 | 38,119,206.265627 |
| pulp_product_odt | 10,824,299.935398 |
| panel_product_m3 | 4,172,197.422276 |
| pellet_product_odt | 4,356,049.838434 |
| bio_product_mwh | 775,428.416180 |
| process_residue_odt | 27,315,295.024382 |
| harvest_residue_gross_odt | 21,103,663.026749 |
| harvest_residue_recoverable_odt | 12,662,197.816048 |
| total_residue_gross_odt | 48,418,958.051121 |
| total_residue_recoverable_odt | 39,977,492.840412 |

Within-class SAW/PANEL and PELLET/BIO splits and mill conversion ratios remain documented donor assumptions. Branch and foliage are dry mass and are never added to stem taper volume.

Labels: `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`.
