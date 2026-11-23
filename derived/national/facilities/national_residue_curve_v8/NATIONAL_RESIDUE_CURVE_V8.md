# National Residue Supply-Curve Sensitivity v8 (Assignment v10)

This forestry-side screening artifact converts the `facility_residue_supply_v8 assignment v10` process and harvest residue streams into availability and recovery scenarios at 18.5 GJ/odt. Process residue is aggregated by facility province and class; harvest residue is aggregated by origin province. The streams remain separate and no combined curve row is written.

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
| SAW | 0.000000 | 59.264 | 118.527 | 177.791 |
| PULP | 0.000000 | 55.879 | 111.759 | 167.638 |
| PANEL | 0.000000 | 5.965 | 11.930 | 17.895 |
| PELLET | 0.000000 | 3.580 | 7.159 | 10.739 |
| BIO | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| TOTAL | 0.000000 | 124.688 | 249.375 | 374.063 |

Base process residue is 26,959,509 odt / 498.751 PJ at the documented LHV.

## National harvest residue (gross and recoverable)

| Recovery case | Recovery | Gross odt | Recoverable odt | Recoverable PJ | Ratio to RSYC 119 Mm3 base |
|---|---:|---:|---:|---:|---:|
| `harvest_recovery_035` | 35% | 24,022,204 | 8,407,771 | 155.544 | 1.1875 |
| `harvest_recovery_060` | 60% | 24,022,204 | 14,413,322 | 266.646 | 2.0358 |
| `harvest_recovery_075` | 75% | 24,022,204 | 18,016,653 | 333.308 | 2.5447 |

## Province process residue (PJ)

| Province | 0% | 25% | 50% | 75% |
|---|---:|---:|---:|---:|
| BC | 0.000000 | 45.503 | 91.005 | 136.508 |
| AB | 0.000000 | 24.969 | 49.939 | 74.908 |
| SK | 0.000000 | 0.238779 | 0.477557 | 0.716336 |
| MB | 0.000000 | 0.759633 | 1.519 | 2.279 |
| ON | 0.000000 | 13.505 | 27.010 | 40.514 |
| QC | 0.000000 | 24.601 | 49.202 | 73.804 |
| NB | 0.000000 | 7.640 | 15.280 | 22.920 |
| NS | 0.000000 | 2.767 | 5.534 | 8.300 |
| PE | 0.000000 | 0.168126 | 0.336252 | 0.504378 |
| NL | 0.000000 | 4.289 | 8.578 | 12.867 |
| YT | 0.000000 | 0.247303 | 0.494606 | 0.741909 |
| NT | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## Province harvest residue (recoverable PJ)

| Province | 35% | 60% | 75% |
|---|---:|---:|---:|
| BC | 41.838 | 71.722 | 89.652 |
| AB | 23.681 | 40.595 | 50.744 |
| SK | 17.861 | 30.619 | 38.273 |
| MB | 1.426 | 2.444 | 3.055 |
| ON | 18.364 | 31.481 | 39.351 |
| QC | 37.567 | 64.401 | 80.501 |
| NB | 7.566 | 12.971 | 16.214 |
| NS | 4.584 | 7.859 | 9.824 |
| PE | 0.465665 | 0.798283 | 0.997854 |
| NL | 2.073 | 3.554 | 4.442 |
| YT | 0.076705 | 0.131494 | 0.164367 |
| NT | 0.041695 | 0.071477 | 0.089346 |
| NU | 0.000000 | 0.000000 | 0.000000 |

## RSYC and OSeCAN comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ. The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ; the familiar 129.6709 PJ figure is that 100 Mm3 reference, not the 119 Mm3 value.

The harvest 60% case is 14,413,322 odt / 266.646 PJ, a ratio of 2.0358 to the RSYC 119 Mm3 base. The 35% and 75% cases bracket it at 1.1875 and 2.5447. Only these harvest recoverable rows are RSYC-comparable.

OSeCAN 2050 context from `data/derived/national/clews/osecan/national_base_119m/dispatch_by_zone.csv` (`stress_119m`): national biomass supply activity 152.923 PJ, BC supply activity 43.524 PJ; national power dispatch 41.108 PJ, BC power dispatch 11.700 PJ. This is model context, not a policy target.

| Comparison (2050) | National PJ | BC PJ |
|---|---:|---:|
| OSeCAN supply-activity context | 152.923 | 43.524 |
| Process residue, 50% availability | 249.375 | 91.005 |
| Harvest residue, 60% recovery | 266.646 | 71.722 |

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

Run `.venv/bin/python -m workflows.national.facilities.national_residue_curve_v8` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_national_facility_chain_v5.py -q` to run the regression tests.

No policy/AAC claim is made.
