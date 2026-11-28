# National RSYC transformed curve library v1

Generated: 2026-11-28T07:36:13Z

## Status and labels

This artifact is a **model estimate** for screening and downstream research. `observed=false`, `policy_grade=false`, `national_claim=false`. It does not replace or mutate official OSeCAN curves, and it does not rebuild WS4.

## Method

RSYC total-volume curves are transformed with the accepted 5-parameter family `V(x)=k*RSYC((x-s)/alpha)` for transformed ages at or above the join, with a ramp toe `k*RSYC(T)*(1-exp(-r*x))/(1-exp(-r*join))` below the join. The vertical `k` is set per curve to preserve the original RSYC volume at age 100 (or the original peak when V100 is not meaningful). Donor-fitted `k` values are never used as merchantability ratios.

BC donor classes were fitted to the dominant-TSA VDYP untreated composites built from the fresh TSA portal and supplemental bundles. The primary fit window is 10-150 years; the 1-250 sensitivity fit is used when the primary alpha reaches its upper bound. QC donor classes were fitted to the 51 BFEC unit composites, the province composite, and the six representative curves, with a post-peak decline/plateau term selected linear -> power -> stretched exponential.

## Extrapolation rule

- BC: BC natural classes, matched by ecoprovince then ecozone then species group.
- QC: QC managed classes, matched by species-mix class (conifer/mixed/deciduous).
- YT/NT/NU: BC natural classes.
- ON/NB/NS/PE/NL: QC managed classes, matched by species mix (no province-specific fit claimed).
- AB/SK/MB: QC managed in Boreal Plains and Boreal Shield ecozones; BC natural elsewhere (Montane Cordillera, Boreal Cordillera, Taiga, Hudson Plains). This is an ecozone-proximity policy, not a province-specific fit.

Every curve carries `donor_class_id`, `donor_distance`, `donor_rule`, and `policy_rule`. Distance rises from 0 (exact ecoprovince + species group) to 5 (BC province fallback) for BC classes and 2-4 for QC mix classes. Distant donors are flagged.

## Donor classes

| class | style | n donors | s | T | alpha | r | decline | R2 median |
|---|---|---:|---:|---:|---:|---:|---|---:|
| BC_natural_Southern_Montane_Cordillera_conifer_mixed | natural_5param | 5 | 45.53 | 6.03 | 1.871 | 0.00001 | none | 0.999 |
| BC_natural_Columbia_Montane_Cordillera_conifer_mixed | natural_5param | 9 | 45.95 | 5.16 | 2.181 | 0.00001 | none | 0.999 |
| BC_natural_Southern_Coastal_Mountains_conifer_mixed | natural_5param | 13 | 23.37 | 2.44 | 3.757 | 0.00001 | none | 0.999 |
| BC_natural_Central_Montane_Cordillera_pine | natural_5param | 3 | 38.12 | 1.26 | 4.298 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Montane_Cordillera_conifer_mixed | natural_5param | 6 | 29.95 | 1.89 | 4.475 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Coastal_Mountains_conifer_mixed | natural_5param | 4 | 60.48 | 4.21 | 1.702 | 0.00001 | none | 0.998 |
| BC_natural_Southern_Boreal_Cordillera_spruce | natural_5param | 7 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_Hay_Slave_Lowlands_spruce | natural_5param | 4 | 22.56 | 4.71 | 2.304 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Boreal_Cordillera_spruce | natural_5param | 3 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_Southern_Montane_Cordillera_conifer | natural_5param | 5 | 45.53 | 6.03 | 1.871 | 0.00001 | none | 0.999 |
| BC_natural_Columbia_Montane_Cordillera_conifer | natural_5param | 9 | 45.95 | 5.16 | 2.181 | 0.00001 | none | 0.999 |
| BC_natural_Southern_Coastal_Mountains_conifer | natural_5param | 13 | 23.37 | 2.44 | 3.757 | 0.00001 | none | 0.999 |
| BC_natural_Central_Montane_Cordillera_conifer | natural_5param | 4 | 35.24 | 5.08 | 3.374 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Montane_Cordillera_conifer | natural_5param | 6 | 29.95 | 1.89 | 4.475 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Coastal_Mountains_conifer | natural_5param | 4 | 60.48 | 4.21 | 1.702 | 0.00001 | none | 0.998 |
| BC_natural_Southern_Boreal_Cordillera_conifer | natural_5param | 9 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_Hay_Slave_Lowlands_conifer | natural_5param | 4 | 22.56 | 4.71 | 2.304 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Boreal_Cordillera_conifer | natural_5param | 4 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_Southern_Montane_Cordillera_all | natural_5param | 5 | 45.53 | 6.03 | 1.871 | 0.00001 | none | 0.999 |
| BC_natural_Columbia_Montane_Cordillera_all | natural_5param | 9 | 45.95 | 5.16 | 2.181 | 0.00001 | none | 0.999 |
| BC_natural_Southern_Coastal_Mountains_all | natural_5param | 13 | 23.37 | 2.44 | 3.757 | 0.00001 | none | 0.999 |
| BC_natural_Boreal_Foothills_all | natural_5param | 3 | 24.72 | 4.94 | 2.151 | 0.00001 | none | 0.999 |
| BC_natural_Central_Montane_Cordillera_all | natural_5param | 4 | 35.24 | 5.08 | 3.374 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Montane_Cordillera_all | natural_5param | 6 | 29.95 | 1.89 | 4.475 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Coastal_Mountains_all | natural_5param | 4 | 60.48 | 4.21 | 1.702 | 0.00001 | none | 0.998 |
| BC_natural_Southern_Boreal_Cordillera_all | natural_5param | 9 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_Hay_Slave_Lowlands_all | natural_5param | 4 | 22.56 | 4.71 | 2.304 | 0.00001 | none | 0.999 |
| BC_natural_Northern_Boreal_Cordillera_all | natural_5param | 4 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_BC_conifer_mixed | natural_5param | 43 | 38.78 | 4.89 | 3.230 | 0.00001 | none | 0.999 |
| BC_natural_BC_pine | natural_5param | 4 | 29.10 | 2.33 | 3.307 | 0.00001 | none | 0.999 |
| BC_natural_BC_deciduous | natural_5param | 3 | 22.51 | 3.47 | 2.908 | 0.00001 | none | 0.999 |
| BC_natural_BC_spruce | natural_5param | 15 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_BC_conifer | natural_5param | 62 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| BC_natural_BC_BC | natural_5param | 65 | 30.79 | 2.96 | 3.647 | 0.00001 | none | 0.999 |
| QC_managed_R01_mixed | managed_extended | 2 | 7.48 | 8.56 | 0.113 | 0.19334 | linear | 0.977 |
| QC_managed_R02_conifer | managed_extended | 6 | 5.74 | 10.13 | 0.176 | 0.02329 | linear | 0.988 |
| QC_managed_R04_conifer | managed_extended | 2 | 6.57 | 5.08 | 0.109 | 0.05355 | linear | 0.984 |
| QC_managed_R03_mixed | managed_extended | 2 | 6.34 | 9.30 | 0.150 | 0.21307 | linear | 0.999 |
| QC_managed_R03_conifer | managed_extended | 2 | 6.82 | 9.83 | 0.135 | 0.03965 | linear | 0.992 |
| QC_managed_R12_mixed | managed_extended | 3 | 4.16 | 10.12 | 0.262 | 0.05152 | linear | 0.999 |
| QC_managed_R04_mixed | managed_extended | 3 | 6.84 | 10.22 | 0.117 | 0.06496 | linear | 0.997 |
| QC_managed_R15_deciduous | managed_extended | 2 | 9.13 | 3.75 | 0.142 | 0.09363 | linear | 0.998 |
| QC_managed_R14_mixed | managed_extended | 2 | 4.15 | 2.16 | 0.186 | 0.02564 | linear | 0.999 |
| QC_managed_R07_deciduous | managed_extended | 3 | 7.30 | 9.92 | 0.169 | 0.07323 | linear | 0.998 |
| QC_managed_R07_mixed | managed_extended | 3 | 6.21 | 13.11 | 0.154 | 0.03564 | linear | 0.999 |
| QC_managed_R08_mixed | managed_extended | 2 | 6.60 | 6.71 | 0.234 | 0.21143 | linear | 0.999 |
| QC_managed_R08_conifer | managed_extended | 4 | 5.86 | 9.00 | 0.152 | 0.04194 | linear | 0.993 |
| QC_managed_R10_conifer | managed_extended | 3 | 4.30 | 11.17 | 0.113 | 0.58004 | stretch | 1.000 |
| QC_managed_R09_conifer | managed_extended | 6 | 5.12 | 7.13 | 0.244 | 0.45514 | power | 0.994 |
| QC_managed_R11_conifer | managed_extended | 3 | 5.85 | 15.28 | 0.100 | 0.05779 | linear | 0.987 |
| QC_managed_R01_all | managed_extended | 2 | 7.48 | 8.56 | 0.113 | 0.19334 | linear | 0.977 |
| QC_managed_R02_all | managed_extended | 7 | 5.74 | 10.13 | 0.176 | 0.02329 | linear | 0.988 |
| QC_managed_R04_all | managed_extended | 5 | 6.57 | 5.08 | 0.109 | 0.05355 | linear | 0.989 |
| QC_managed_R03_all | managed_extended | 4 | 6.49 | 8.86 | 0.152 | 0.07103 | linear | 0.998 |
| QC_managed_R12_all | managed_extended | 3 | 4.16 | 10.12 | 0.262 | 0.05152 | linear | 0.999 |
| QC_managed_R15_all | managed_extended | 3 | 9.13 | 3.75 | 0.142 | 0.09363 | linear | 0.998 |
| QC_managed_R14_all | managed_extended | 2 | 4.15 | 2.16 | 0.186 | 0.02564 | linear | 0.999 |
| QC_managed_R07_all | managed_extended | 6 | 7.30 | 9.92 | 0.169 | 0.07323 | linear | 0.999 |
| QC_managed_R08_all | managed_extended | 6 | 5.86 | 9.00 | 0.152 | 0.04194 | linear | 0.997 |
| QC_managed_R10_all | managed_extended | 3 | 4.30 | 11.17 | 0.113 | 0.58004 | stretch | 1.000 |
| QC_managed_R09_all | managed_extended | 6 | 5.12 | 7.13 | 0.244 | 0.45514 | power | 0.994 |
| QC_managed_R11_all | managed_extended | 3 | 5.85 | 15.28 | 0.100 | 0.05779 | linear | 0.987 |
| QC_managed_QC_mixed | managed_extended | 20 | 6.34 | 9.30 | 0.150 | 0.21307 | linear | 0.999 |
| QC_managed_QC_conifer | managed_extended | 26 | 6.18 | 10.60 | 0.162 | 0.04577 | linear | 0.982 |
| QC_managed_QC_deciduous | managed_extended | 5 | 9.36 | 2.65 | 0.154 | 0.07006 | linear | 0.998 |
| QC_managed_QC_all | managed_extended | 51 | 6.18 | 10.60 | 0.162 | 0.04577 | linear | 0.996 |

## Fit quality

BC tile fits: 65 of 65 produced a VDYP composite; primary R2 min 0.9977. Poor fits (R2 < 0.90): 0.

QC unit fits: 51 of 51; selected full-curve R2 median 0.9974, min 0.9596. Poor fits (R2 < 0.90): 0.

## National library and CMAI

Curves: 3,948; rows: 789,600; provinces: 13; species codes: 12.

### CMAI before and after by province and species group

| province | species group | n | raw CMAI median | transformed CMAI median | raw CMAI age median | transformed CMAI age median |
|---|---|---:|---:|---:|---:|---:|
| AB | conifer_mixed | 9 | 7.38 | 2.64 | 2 | 121 |
| AB | deciduous | 38 | 3.55 | 2.17 | 24 | 119 |
| AB | fir | 57 | 4.91 | 2.88 | 2 | 111 |
| AB | larch | 38 | 4.59 | 2.56 | 2 | 111 |
| AB | pine | 85 | 4.40 | 2.56 | 2 | 103 |
| AB | spruce | 73 | 3.07 | 2.88 | 25 | 111 |
| BC | conifer_mixed | 54 | 8.06 | 2.79 | 2 | 116 |
| BC | deciduous | 65 | 4.15 | 2.36 | 24 | 119 |
| BC | fir | 103 | 6.92 | 2.54 | 2 | 111 |
| BC | larch | 57 | 6.71 | 2.31 | 2 | 111 |
| BC | pine | 124 | 5.81 | 2.23 | 2 | 109 |
| BC | spruce | 82 | 3.67 | 1.82 | 25 | 161 |
| MB | deciduous | 39 | 2.32 | 1.55 | 24 | 100 |
| MB | fir | 39 | 2.20 | 1.01 | 2 | 111 |
| MB | larch | 39 | 2.20 | 1.01 | 2 | 111 |
| MB | pine | 90 | 2.10 | 1.43 | 2 | 103 |
| MB | spruce | 78 | 1.96 | 1.25 | 25 | 111 |
| NB | conifer_mixed | 11 | 4.70 | 12.09 | 2 | 13 |
| NB | deciduous | 11 | 3.96 | 10.24 | 24 | 18 |
| NB | fir | 11 | 3.52 | 11.43 | 13 | 13 |
| NB | larch | 11 | 4.70 | 12.09 | 2 | 13 |
| NB | pine | 33 | 4.70 | 12.09 | 2 | 13 |
| NB | spruce | 11 | 2.77 | 11.13 | 25 | 15 |
| NL | deciduous | 40 | 1.54 | 3.45 | 13 | 17 |
| NL | fir | 40 | 1.68 | 5.26 | 13 | 13 |
| NL | larch | 40 | 2.08 | 5.36 | 2 | 13 |
| NL | pine | 65 | 2.09 | 5.39 | 2 | 13 |
| NL | spruce | 80 | 1.54 | 5.17 | 14 | 14 |
| NS | conifer_mixed | 10 | 3.82 | 9.83 | 2 | 13 |
| NS | deciduous | 10 | 3.04 | 7.84 | 24 | 18 |
| NS | fir | 10 | 2.40 | 7.80 | 13 | 13 |
| NS | larch | 10 | 3.82 | 9.83 | 2 | 13 |
| NS | pine | 30 | 3.47 | 9.61 | 2 | 13 |
| NS | spruce | 10 | 2.04 | 8.19 | 25 | 15 |
| NT | deciduous | 67 | 1.45 | 0.75 | 24 | 119 |
| NT | fir | 37 | 1.84 | 0.66 | 2 | 111 |
| NT | larch | 67 | 1.58 | 0.55 | 2 | 111 |
| NT | pine | 129 | 1.51 | 0.61 | 2 | 103 |
| NT | spruce | 134 | 1.06 | 0.55 | 25 | 161 |
| NU | deciduous | 57 | 0.93 | 0.43 | 13 | 100 |
| NU | fir | 20 | 1.53 | 0.53 | 2 | 111 |
| NU | larch | 57 | 1.22 | 0.42 | 2 | 111 |
| NU | pine | 86 | 1.21 | 0.45 | 2 | 103 |
| NU | spruce | 114 | 0.95 | 0.44 | 25 | 161 |
| ON | deciduous | 59 | 2.87 | 7.41 | 24 | 18 |
| ON | fir | 59 | 3.47 | 8.93 | 2 | 13 |
| ON | larch | 59 | 3.51 | 9.03 | 2 | 13 |
| ON | pine | 175 | 2.80 | 8.25 | 2 | 13 |
| ON | spruce | 118 | 2.53 | 8.95 | 14 | 14 |
| PE | conifer_mixed | 6 | 3.51 | 9.04 | 2 | 13 |
| PE | deciduous | 6 | 2.99 | 7.72 | 24 | 18 |
| PE | fir | 6 | 2.62 | 8.49 | 13 | 13 |
| PE | larch | 6 | 3.51 | 9.04 | 2 | 13 |
| PE | pine | 18 | 3.51 | 9.04 | 2 | 13 |
| PE | spruce | 6 | 2.14 | 8.59 | 25 | 15 |
| QC | conifer_mixed | 15 | 4.83 | 12.43 | 2 | 13 |
| QC | deciduous | 93 | 1.85 | 4.26 | 24 | 18 |
| QC | fir | 90 | 2.03 | 5.55 | 2 | 13 |
| QC | larch | 93 | 2.30 | 5.93 | 2 | 13 |
| QC | pine | 205 | 2.53 | 6.88 | 2 | 13 |
| QC | spruce | 178 | 1.68 | 5.46 | 25 | 15 |
| SK | conifer_mixed | 3 | 7.43 | 2.61 | 2 | 121 |
| SK | deciduous | 32 | 2.74 | 1.69 | 24 | 119 |
| SK | fir | 35 | 2.41 | 1.44 | 2 | 111 |
| SK | larch | 32 | 2.29 | 1.24 | 2 | 111 |
| SK | pine | 62 | 1.44 | 1.39 | 2 | 103 |
| SK | spruce | 61 | 1.69 | 1.41 | 25 | 111 |
| YT | conifer_mixed | 2 | 1.52 | 0.55 | 2 | 124 |
| YT | deciduous | 38 | 1.78 | 0.89 | 24 | 119 |
| YT | fir | 34 | 2.38 | 0.82 | 2 | 111 |
| YT | larch | 38 | 2.38 | 0.82 | 2 | 111 |
| YT | pine | 72 | 2.37 | 0.83 | 2 | 103 |
| YT | spruce | 76 | 1.39 | 0.93 | 25 | 161 |

## Raw 2-year and 24-year CMAI artifacts

Raw CMAI age counts: age 2 = 2,250; age 24 = 342. After transformation: age 2 = 0; age 24 = 0. Curves whose artefact was removed: 2,592.

The new transformed CMAI age distribution by province is in `qc_summary.csv` and `summary.json`; the modal spikes at 2 and 24 years are absent.

## QC gate

Pass: 2,383; flag: 1,565; fail: 0. Failures are retained in `transformed_curves.csv` with a reason; no curve is silently dropped or replaced.

Top reasons:
- `distant_donor`: 1,565

### Step 4 consumption contract

Use `usable=true` rows: **3,948 of 3,948 curves** (100.0%). `pass` and `flag` are both usable; `flag` records provenance (chiefly distant donor) and does not mean the curve is rejected. `fail` rows are not usable; this build has 0.

CMAI bands by donor basis (soft -> flag, hard -> fail):
- soft `natural_5param|conifer`: 0.20-8.00
- soft `natural_5param|deciduous`: 0.20-8.00
- soft `managed_extended|conifer`: 1.00-30.00
- soft `managed_extended|deciduous`: 1.00-20.00
- hard `natural_5param`: 0.10-10.00
- hard `managed_extended`: 0.50-35.00

### Peak and decline rules

Natural 5-parameter donors carry no forced decline; their transformed curves may still rise to age 200. Managed AAC donors start the fitted decline/plateau at the donor-basis peak age (20-32 yr in this build) and flatten at the fitted flat age (50-55 yr), so managed curves do not rise to age 200 even when the underlying RSYC b4 coefficient is negative.

## Basis quarantine for managed curves

All 1,926 `managed_extended` curves are quarantined as basis
artifacts. The QC BFEC donor is a managed/AAC-like net merchantable volume, not
a VDYP/RSYC total volume. The donor plateaus by age 45-50, its alpha (~0.15)
maps stand age 13 to raw age ~42, and same-age volume is 2.6-3.2x the raw RSYC
curve. In `curve_metadata.csv`, these rows carry `basis_mismatch=true`,
`usable_total_volume=false`, and `comparable_total_volume=false`; provenance
columns are retained. All 2,022 `natural_5param` curves remain
usable.

Use `usable_total_volume=true` rows for total-volume work: do not use
`managed_extended` rows as total volume even where `usable=true`. The corrected
feed is `national_rsyc_transform_natural_v1`, which rebuilds every cell with a
`natural_5param` donor and preserves V100.

## Limitations

- The transform is a shape donor transfer, not a species-specific yield model. It must not be read as a province-specific fitted curve where no BC/QC reference exists.
- QC units lack a public ecozone join in this build; QC donor classes are therefore matched by species mix, and `donor_distance` records that limitation.
- AB/SK/MB managed/natural assignment is an ecozone policy choice documented above; it is not a local calibration.
- The alpha floor (0.35 for QC) keeps the mapped RSYC age inside its published domain. As a result, managed donor peaks land near 45-60 years rather than the 20-30 year BFEC peaks; CMAI remains in the QC observed range and the QC gate checks it.
- No WS4 rebuild and no OSeCAN mutation are part of this artifact.

## Reproduction

Build: `python scripts/national/build_rsyc_transform_v1.py`. Tests: `pytest tests/test_rsyc_transform_v1.py`.
