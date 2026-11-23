# National Residue Supply-Curve Sensitivity v6 (E1+E2)

This forestry-side screening artifact converts the `facility_residue_supply_v6` process and harvest residue streams into availability and recovery scenarios at 18.5 GJ/odt. Process residue is aggregated by facility province and class; harvest residue is aggregated by origin province. The streams remain separate and no combined curve row is written.

All values are model estimates: `model_estimate=true`, `observed=false`, `policy_grade=false`, `not_policy=true`. `rsyc_comparable=true` appears only on harvest recoverable rows. The artifact is not an operating, policy, AAC, tenure, or investment statement.

## Scenario definitions

| Family | Case | Fraction | Basis |
|---|---|---:|---|
| Process availability | `process_availability_000` | 0% | Facility process residue, each class and total |
| Process availability | `process_availability_025` | 25% | Facility process residue, each class and total |
| Process availability | `process_availability_050` | 50% | Facility process residue, each class and total |
| Process availability | `process_availability_075` | 75% | Facility process residue, each class and total |
| Harvest recovery | `harvest_recovery_035` | 35% | Gross harvest residue by origin province |
| Harvest recovery | `harvest_recovery_060` | 60% | Gross harvest residue by origin province |
| Harvest recovery | `harvest_recovery_075` | 75% | Gross harvest residue by origin province |

The process availability fraction is applied uniformly to every class in a case; the class rows let a reader reinterpret the fraction class by class, and the `TOTAL` row is the sum of the mutually exclusive classes at the same fraction. Harvest recovery is applied to gross harvest residue, not to the already recoverable base.

## National process residue (PJ)

| Class | 0% | 25% | 50% | 75% |
|---|---:|---:|---:|---:|
| SAW | 0.000000 | 66.528 | 133.056 | 199.584 |
| PULP | 0.000000 | 50.128 | 100.255 | 150.383 |
| PANEL | 0.000000 | 6.696 | 13.392 | 20.088 |
| PELLET | 0.000000 | 2.982 | 5.963 | 8.945 |
| BIO | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| TOTAL | 0.000000 | 126.333 | 252.666 | 379.000 |

Base process residue is 27,315,295 odt / 505.333 PJ at the documented LHV.

## National harvest residue (gross and recoverable)

| Recovery case | Recovery | Gross odt | Recoverable odt | Recoverable PJ | Ratio to RSYC 119 Mm3 base |
|---|---:|---:|---:|---:|---:|
| `harvest_recovery_035` | 35% | 21,103,663 | 7,386,282 | 136.646 | 1.0433 |
| `harvest_recovery_060` | 60% | 21,103,663 | 12,662,198 | 234.251 | 1.7884 |
| `harvest_recovery_075` | 75% | 21,103,663 | 15,827,747 | 292.813 | 2.2355 |

## Province process residue (PJ)

| Province | 0% | 25% | 50% | 75% |
|---|---:|---:|---:|---:|
| BC | 0.000000 | 44.921 | 89.843 | 134.764 |
| AB | 0.000000 | 25.886 | 51.771 | 77.657 |
| SK | 0.000000 | 2.162 | 4.323 | 6.485 |
| MB | 0.000000 | 0.662546 | 1.325 | 1.988 |
| ON | 0.000000 | 13.894 | 27.789 | 41.683 |
| QC | 0.000000 | 28.811 | 57.622 | 86.433 |
| NB | 0.000000 | 6.514 | 13.028 | 19.542 |
| NS | 0.000000 | 2.452 | 4.904 | 7.356 |
| PE | 0.000000 | 0.123435 | 0.246870 | 0.370305 |
| NL | 0.000000 | 0.887313 | 1.775 | 2.662 |
| YT | 0.000000 | 0.019783 | 0.039565 | 0.059348 |
| NT | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## Province harvest residue (recoverable PJ)

| Province | 35% | 60% | 75% |
|---|---:|---:|---:|
| BC | 41.838 | 71.722 | 89.652 |
| AB | 19.642 | 33.672 | 42.090 |
| SK | 4.749 | 8.141 | 10.176 |
| MB | 1.603 | 2.748 | 3.435 |
| ON | 18.143 | 31.102 | 38.878 |
| QC | 37.567 | 64.401 | 80.501 |
| NB | 7.566 | 12.971 | 16.214 |
| NS | 2.992 | 5.129 | 6.412 |
| PE | 0.360270 | 0.617606 | 0.772008 |
| NL | 2.068 | 3.546 | 4.432 |
| YT | 0.076705 | 0.131494 | 0.164367 |
| NT | 0.040955 | 0.070208 | 0.087760 |
| NU | 0.000000 | 0.000000 | 0.000000 |

## RSYC and OSeCAN comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ. The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ; the familiar 129.6709 PJ figure is that 100 Mm3 reference, not the 119 Mm3 value.

The harvest 60% case is 12,662,198 odt / 234.251 PJ, a ratio of 1.7884 to the RSYC 119 Mm3 base. The 35% and 75% cases bracket it at 1.0433 and 2.2355. Only these harvest recoverable rows are RSYC-comparable.

OSeCAN 2050 context from `data/derived/national/clews/osecan/national_base_119m/dispatch_by_zone.csv` (`stress_119m`): national biomass supply activity 152.923 PJ, BC supply activity 43.524 PJ; national power dispatch 41.108 PJ, BC power dispatch 11.700 PJ. This is model context, not a policy target.

| Comparison (2050) | National PJ | BC PJ |
|---|---:|---:|
| OSeCAN supply-activity context | 152.923 | 43.524 |
| Process residue, 50% availability | 252.666 | 89.843 |
| Harvest residue, 60% recovery | 234.251 | 71.722 |

Process residue is not added to the RSYC comparison. The process and harvest streams are not summed into a combined curve row; any combined interpretation must add them explicitly outside this artifact.

## Caveats

- Process residue is facility process residue aggregated by facility province and class; it is not a measured mill-by-mill availability survey.
- The 0/25/50/75% process availability cases are screening fractions, not observed availability or policy targets.
- Harvest recoverable residue is gross harvest residue times a recovery fraction; it is not facility-assigned and is not a harvest-level forecast.
- The parent artifact's `harvest_residue_recoverable` row is the product-chain residue-feedstock volume, not the 0.60 recovery scenario; this curve applies the documented 0.35/0.60/0.75 recovery fractions to gross harvest residue.
- The process stream and harvest stream are physically distinct here; the artifact does not add them into a single curve.
- Facility process residue includes residue generated from class feedstock that may itself contain residue feedstock; this is a cascade, not a second count of the same provincial harvest residue.
- OSeCAN context uses `stress_119m`, the manifest's informative supply case; `baseline_119m` is a controlled zero-biomass reference.
- OSeCAN supply activity is used as the biomass-demand context; power dispatch is shown separately and is not the same quantity.
- Conversion uses the RSYC dry LHV of 18.5 GJ/odt; no moisture, bark, or heat-rate adjustment is applied.
- The usual 129.6709 PJ figure is the RSYC 100 Mm3 base, not the 119 Mm3 base.
- No transport, cost, revenue, capacity-expansion, tenure, AAC, or policy claim is made. No UI or public OSeCAN surface is changed.

## Tests and status

Build status: `pass`. Validation checks: 14, failed: 0.

Run `.venv/bin/python -m workflows.national.facilities.national_residue_curve_v6` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_national_residue_curve_v6.py -q` to run the regression tests.

No policy/AAC claim is made.
