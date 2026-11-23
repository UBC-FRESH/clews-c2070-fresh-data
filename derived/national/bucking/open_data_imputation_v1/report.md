# Open-data tree-list imputation for the nine non-measured provinces

**Status:** E2 open-data imputation; `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`. No DUA, request or restricted data used.

## Method

SCANFI v2 province species composition sets species shares. Donor DBH/height pairs are drawn deterministically from measured BC/QC/NB/YT stems. Published BC Kozak (2004) or QC Schneider (2013) tapers are used as cross-jurisdiction donors; the national pilot dimension-only sorts and the existing bucking/residue engine are applied unchanged.
Each imputed province has 36 representative stems. Expansion totals 1000 stems/ha, a round representative density, so expanded volume is a per-hectare quantity without calibration. Product shares and residue per recovered m3 are scale-free. E2 residue includes CFS branch and foliage allometry; the 13-province coefficient table is E1 measured for BC/QC/NB/YT and E2 imputed for the other nine.

## Coverage

| Province | Tier | Trees | Basis | Taper donor | Allometry |
|---|---|---:|---|---|---|
| BC | E1_measured_tree_list | 347 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper | CFS tree-level DBH+height branch/foliage (E1 measured stems) |
| AB | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Black spruce;Conifers;Deciduous;Jack pine;Lodgepole pine;Tamarack larch |
| SK | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Black spruce;Conifers;Deciduous;Jack pine;Tamarack larch |
| MB | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Balsam fir;Black spruce;Conifers;Deciduous;Jack pine;Tamarack larch |
| ON | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Balsam fir;Black spruce;Conifers;Deciduous;Eastern white pine;Jack pine;Tamarack larch |
| QC | E1_measured_tree_list | 85 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper | CFS tree-level DBH+height branch/foliage (E1 measured stems) |
| NB | E1_measured_tree_list | 106 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper | CFS tree-level DBH+height branch/foliage (E1 measured stems) |
| NS | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC | CFS tree-level DBH+height branch/foliage; Balsam fir;Black spruce;Conifers;Deciduous;Eastern white pine;Tamarack larch |
| PE | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC | CFS tree-level DBH+height branch/foliage; Balsam fir;Black spruce;Conifers;Deciduous;Eastern white pine;Jack pine;Tamarack larch |
| NL | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC | CFS tree-level DBH+height branch/foliage; Balsam fir;Black spruce;Conifers;Deciduous;Tamarack larch |
| YT | E1_measured_tree_list | 53 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper | CFS tree-level DBH+height branch/foliage (E1 measured stems) |
| NT | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Black spruce;Conifers;Deciduous;Jack pine;Lodgepole pine;Tamarack larch |
| NU | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC | CFS tree-level DBH+height branch/foliage; Black spruce;Conifers;Deciduous;Jack pine;Tamarack larch |

## E1/E2 product coefficients

Solid is the sawlog-grade share, pulp is the pulpwood share, and other is other roundwood. Within-class SAW/PANEL and PELLET/BIO splits and mill conversion ratios remain documented donor assumptions.

| Province | Tier | Solid | Pulp | Other | Stem ODT/m3 | Branch+foliage ODT/m3 | Total ODT/m3 | Rec 0.60 ODT/m3 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BC | measured_bucking_pilot | 0.6953 | 0.2948 | 0.0100 | 0.040577 | 0.121045 | 0.161622 | 0.096973 |
| AB | e2_open_data_imputation | 0.5985 | 0.3773 | 0.0242 | 0.040511 | 0.092006 | 0.132517 | 0.079510 |
| SK | e2_open_data_imputation | 0.4704 | 0.5008 | 0.0288 | 0.063432 | 0.105375 | 0.168808 | 0.101285 |
| MB | e2_open_data_imputation | 0.5099 | 0.4611 | 0.0290 | 0.094930 | 0.123141 | 0.218071 | 0.130842 |
| ON | e2_open_data_imputation | 0.4529 | 0.5076 | 0.0396 | 0.083483 | 0.124172 | 0.207654 | 0.124593 |
| QC | measured_bucking_pilot | 0.3420 | 0.6417 | 0.0164 | 0.059410 | 0.158097 | 0.217507 | 0.130504 |
| NB | measured_bucking_pilot | 0.5238 | 0.4672 | 0.0090 | 0.030341 | 0.157085 | 0.187426 | 0.112456 |
| NS | e2_open_data_imputation | 0.4080 | 0.5754 | 0.0166 | 0.038670 | 0.154820 | 0.193490 | 0.116094 |
| PE | e2_open_data_imputation | 0.3840 | 0.5908 | 0.0252 | 0.034972 | 0.149139 | 0.184111 | 0.110466 |
| NL | e2_open_data_imputation | 0.5103 | 0.4873 | 0.0024 | 0.065621 | 0.154070 | 0.219691 | 0.131814 |
| YT | measured_bucking_pilot | 0.4246 | 0.5625 | 0.0129 | 0.123046 | 0.146642 | 0.269689 | 0.161813 |
| NT | e2_open_data_imputation | 0.6242 | 0.3589 | 0.0169 | 0.070509 | 0.103371 | 0.173880 | 0.104328 |
| NU | e2_open_data_imputation | 0.7051 | 0.2816 | 0.0132 | 0.137096 | 0.137126 | 0.274223 | 0.164534 |

## Logs and residue

| Province | Logs | Recovered m3/ha-eq | Residue m3 | Residue ODT | Sawlog | Pulp | Other | Solid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 1238 | 165127.42 | 17506.42 | 26688.22 | 0.695 | 0.295 | 0.010 | 0.705 |
| AB | 62 | 161.37 | 17.32 | 21.38 | 0.598 | 0.377 | 0.024 | 0.623 |
| SK | 56 | 120.01 | 19.85 | 20.26 | 0.470 | 0.501 | 0.029 | 0.499 |
| MB | 43 | 96.37 | 23.70 | 21.02 | 0.510 | 0.461 | 0.029 | 0.539 |
| ON | 50 | 100.31 | 22.26 | 20.83 | 0.453 | 0.508 | 0.040 | 0.492 |
| QC | 319 | 266152.64 | 40986.60 | 57890.07 | 0.342 | 0.642 | 0.016 | 0.358 |
| NB | 380 | 374151.71 | 30623.28 | 70125.82 | 0.524 | 0.467 | 0.009 | 0.533 |
| NS | 87 | 202.68 | 19.23 | 39.22 | 0.408 | 0.575 | 0.017 | 0.425 |
| PE | 91 | 223.80 | 18.20 | 41.20 | 0.384 | 0.591 | 0.025 | 0.409 |
| NL | 62 | 153.49 | 24.82 | 33.72 | 0.510 | 0.487 | 0.002 | 0.513 |
| YT | 160 | 30615.18 | 9659.42 | 8256.57 | 0.425 | 0.563 | 0.013 | 0.437 |
| NT | 45 | 123.12 | 22.44 | 21.41 | 0.624 | 0.359 | 0.017 | 0.641 |
| NU | 29 | 75.46 | 26.94 | 20.69 | 0.705 | 0.282 | 0.013 | 0.718 |

## Facility coefficient fit

| Province | Model solid | Facility solid | Solid ratio | Model residue ODT/m3 | Facility residue ODT/m3 | Fit | Dominance flag |
|---|---:|---:|---:|---:|---:|---|---|
| BC | 0.705 | 0.705 | 1.000 | 0.1616 | 0.1616 | within_20pct | measured_facility_coefficient |
| AB | 0.623 | 1.000 | 0.623 | 0.1325 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| SK | 0.499 | 1.000 | 0.499 | 0.1688 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| MB | 0.539 | 1.000 | 0.539 | 0.2181 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| ON | 0.492 | 1.000 | 0.493 | 0.2077 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| QC | 0.358 | 0.358 | 1.000 | 0.2175 | 0.2175 | within_20pct | measured_facility_coefficient |
| NB | 0.533 | 0.533 | 1.000 | 0.1874 | 0.1874 | within_20pct | measured_facility_coefficient |
| NS | 0.425 | 1.000 | 0.425 | 0.1935 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| PE | 0.409 | 1.000 | 0.409 | 0.1841 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| NL | 0.513 | 1.000 | 0.513 | 0.2197 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| YT | 0.437 | 0.437 | 1.000 | 0.2697 | 0.2697 | within_20pct | measured_facility_coefficient |
| NT | 0.641 | 1.000 | 0.641 | 0.1739 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| NU | 0.718 | 0.000 | 0.000 | 0.2742 | 0.0000 | no_modelled_harvest | not_applicable_no_harvest |

Facility shares are donor feedstock coefficients; E2 shares are the imputed product coefficients. Harvest and process residue are different streams. E2 residue now includes CFS branch and foliage, so the residue comparison is like-for-like. Divergence is reported, not tuned away.

## Aggregate checks

- NFI national tree volume: 51073.6 million m3.
- NFI national above-ground biomass: 30525.2 million t.
- NFI forest land: 369019352 ha.
- RSYC age-100 mean volume is an aggregate context check, never a calibration target.

## Limits

- E2 is not E1. Province composition is SCANFI-modelled, donor geometry is not local.
- No local taper, local DBH distribution, defect, grade, sweep, knot or rot measurement exists for the nine imputed jurisdictions.
- The facility comparison is a screening check, not a supply estimate or official grade assignment.
- NU is represented for 13-province coverage but has no modelled harvest in the 119 Mm3 case.
