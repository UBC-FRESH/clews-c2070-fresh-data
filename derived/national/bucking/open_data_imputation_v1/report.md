# Open-data tree-list imputation for the nine non-measured provinces

**Status:** E2 open-data imputation; `model_estimate=true`, `observed=false`, `policy_grade=false`, `national_claim=false`. No DUA, request or restricted data used.

## Method

SCANFI v2 province species composition sets species shares. Donor DBH/height pairs are drawn deterministically from measured BC/QC/NB/YT stems. Published BC Kozak (2004) or QC Schneider (2013) tapers are used as cross-jurisdiction donors; the national pilot dimension-only sorts and the existing bucking/residue engine are applied unchanged.
Each imputed province has 36 representative stems. Expansion totals 1000 stems/ha, a round representative density, so expanded volume is a per-hectare quantity without calibration. Product shares and residue per recovered m3 are scale-free. Imputed residue is stem-only.

## Coverage

| Province | Tier | Trees | Basis | Taper donor |
|---|---|---:|---|---|
| BC | E1_measured_tree_list | 347 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper |
| AB | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |
| SK | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |
| MB | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |
| ON | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |
| QC | E1_measured_tree_list | 85 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper |
| NB | E1_measured_tree_list | 106 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper |
| NS | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC |
| PE | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC |
| NL | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC;QC |
| YT | E1_measured_tree_list | 53 | four_province_bucking_pilot_v0_measured | local BC/QC or donor QC/BC published taper |
| NT | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |
| NU | E2_open_data_imputation | 36 | scanfi_v2_composition_plus_measured_donor_geometry | donor published tapers: BC |

## Logs and residue

| Province | Logs | Recovered m3/ha-eq | Residue m3 | Residue ODT | Sawlog | Pulp | Other | Solid |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| BC | 1238 | 165127.42 | 17506.42 | 26688.22 | 0.695 | 0.295 | 0.010 | 0.705 |
| AB | 62 | 161.37 | 17.32 | 6.54 | 0.598 | 0.377 | 0.024 | 0.623 |
| SK | 56 | 120.01 | 19.85 | 7.61 | 0.470 | 0.501 | 0.029 | 0.499 |
| MB | 43 | 96.37 | 23.70 | 9.15 | 0.510 | 0.461 | 0.029 | 0.539 |
| ON | 50 | 100.31 | 22.26 | 8.37 | 0.453 | 0.508 | 0.040 | 0.492 |
| QC | 319 | 266152.64 | 40986.60 | 57890.07 | 0.342 | 0.642 | 0.016 | 0.358 |
| NB | 380 | 374151.71 | 30623.28 | 70125.82 | 0.524 | 0.467 | 0.009 | 0.533 |
| NS | 87 | 202.68 | 19.23 | 7.84 | 0.408 | 0.575 | 0.017 | 0.425 |
| PE | 91 | 223.80 | 18.20 | 7.83 | 0.384 | 0.591 | 0.025 | 0.409 |
| NL | 62 | 153.49 | 24.82 | 10.07 | 0.510 | 0.487 | 0.002 | 0.513 |
| YT | 160 | 30615.18 | 9659.42 | 8256.57 | 0.425 | 0.563 | 0.013 | 0.437 |
| NT | 45 | 123.12 | 22.44 | 8.68 | 0.624 | 0.359 | 0.017 | 0.641 |
| NU | 29 | 75.46 | 26.94 | 10.35 | 0.705 | 0.282 | 0.013 | 0.718 |

## Facility coefficient fit

| Province | Model solid | Facility solid | Solid ratio | Model residue ODT/m3 | Facility residue ODT/m3 | Fit | Dominance flag |
|---|---:|---:|---:|---:|---:|---|---|
| BC | 0.705 | 0.705 | 1.000 | 0.1616 | 0.1616 | within_20pct | measured_facility_coefficient |
| AB | 0.623 | 1.000 | 0.623 | 0.0405 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| SK | 0.499 | 1.000 | 0.499 | 0.0634 | 0.0762 | partial | donor_coefficient_vs_imputation_diverge |
| MB | 0.539 | 1.000 | 0.539 | 0.0949 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| ON | 0.492 | 1.000 | 0.493 | 0.0835 | 0.0762 | partial | donor_coefficient_vs_imputation_diverge |
| QC | 0.358 | 0.358 | 1.000 | 0.2175 | 0.2175 | within_20pct | measured_facility_coefficient |
| NB | 0.533 | 0.533 | 1.000 | 0.1874 | 0.1874 | within_20pct | measured_facility_coefficient |
| NS | 0.425 | 1.000 | 0.425 | 0.0387 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| PE | 0.409 | 1.000 | 0.409 | 0.0350 | 0.0762 | outside_20pct | donor_coefficient_vs_imputation_diverge |
| NL | 0.513 | 1.000 | 0.513 | 0.0656 | 0.0762 | partial | donor_coefficient_vs_imputation_diverge |
| YT | 0.437 | 0.437 | 1.000 | 0.2697 | 0.2697 | within_20pct | measured_facility_coefficient |
| NT | 0.641 | 1.000 | 0.641 | 0.0705 | 0.0762 | partial | donor_coefficient_vs_imputation_diverge |
| NU | 0.718 | 0.000 | 0.000 | 0.1371 | 0.0000 | no_modelled_harvest | not_applicable_no_harvest |

Facility shares are feedstock coefficients; harvest and process residue are different streams. E2 residue is stem-only, so the residue comparison is a lower-bound screening check. Divergence is reported, not tuned away.

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
