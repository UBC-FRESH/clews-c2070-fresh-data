# National Residue Supply-Curve Sensitivity v4

This forestry-side screening artifact converts the `facility_residue_supply_v4` process and harvest residue streams into availability and recovery scenarios at 18.5 GJ/odt. Process residue is aggregated by facility province and class; harvest residue is aggregated by origin province. The streams remain separate and no combined curve row is written.

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
| SAW | 0.000000 | 74.209 | 148.417 | 222.626 |
| PULP | 0.000000 | 44.120 | 88.239 | 132.359 |
| PANEL | 0.000000 | 7.469 | 14.938 | 22.408 |
| PELLET | 0.000000 | 2.856 | 5.712 | 8.568 |
| BIO | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| TOTAL | 0.000000 | 128.654 | 257.307 | 385.961 |

Base process residue is 27,816,974 odt / 514.614 PJ at the documented LHV.

## National harvest residue (gross and recoverable)

| Recovery case | Recovery | Gross odt | Recoverable odt | Recoverable PJ | Ratio to RSYC 119 Mm3 base |
|---|---:|---:|---:|---:|---:|
| `harvest_recovery_035` | 35% | 6,911,364 | 2,418,977 | 44.751 | 0.3417 |
| `harvest_recovery_060` | 60% | 6,911,364 | 4,146,818 | 76.716 | 0.5857 |
| `harvest_recovery_075` | 75% | 6,911,364 | 5,183,523 | 95.895 | 0.7321 |

## Province process residue (PJ)

| Province | 0% | 25% | 50% | 75% |
|---|---:|---:|---:|---:|
| BC | 0.000000 | 45.068 | 90.135 | 135.203 |
| AB | 0.000000 | 26.687 | 53.374 | 80.060 |
| SK | 0.000000 | 3.161 | 6.323 | 9.484 |
| MB | 0.000000 | 0.856948 | 1.714 | 2.571 |
| ON | 0.000000 | 14.286 | 28.572 | 42.857 |
| QC | 0.000000 | 28.796 | 57.592 | 86.388 |
| NB | 0.000000 | 6.453 | 12.905 | 19.358 |
| NS | 0.000000 | 2.531 | 5.062 | 7.593 |
| PE | 0.000000 | 0.219894 | 0.439789 | 0.659683 |
| NL | 0.000000 | 0.575582 | 1.151 | 1.727 |
| YT | 0.000000 | 0.019973 | 0.039945 | 0.059918 |
| NT | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| NU | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

## Province harvest residue (recoverable PJ)

| Province | 35% | 60% | 75% |
|---|---:|---:|---:|
| BC | 10.504 | 18.006 | 22.508 |
| AB | 11.298 | 19.368 | 24.211 |
| SK | 2.144 | 3.676 | 4.595 |
| MB | 0.560307 | 0.960527 | 1.201 |
| ON | 6.660 | 11.417 | 14.271 |
| QC | 10.261 | 17.590 | 21.988 |
| NB | 1.225 | 2.100 | 2.625 |
| NS | 1.179 | 2.021 | 2.526 |
| PE | 0.149159 | 0.255701 | 0.319626 |
| NL | 0.717655 | 1.230 | 1.538 |
| YT | 0.034997 | 0.059994 | 0.074993 |
| NT | 0.017954 | 0.030778 | 0.038472 |
| NU | 0.000000 | 0.000000 | 0.000000 |

## RSYC and OSeCAN comparison

RSYC 119 Mm3 base recoverable residue is 7,080,062 odt / 130.981 PJ. The documented RSYC 100 Mm3 base is 7,009,238 odt / 129.671 PJ; the familiar 129.6709 PJ figure is that 100 Mm3 reference, not the 119 Mm3 value.

The harvest 60% case is 4,146,818 odt / 76.716 PJ, a ratio of 0.5857 to the RSYC 119 Mm3 base. The 35% and 75% cases bracket it at 0.3417 and 0.7321. Only these harvest recoverable rows are RSYC-comparable.

OSeCAN 2050 context from `data/derived/national/clews/osecan/national_base_119m/dispatch_by_zone.csv` (`stress_119m`): national biomass supply activity 152.923 PJ, BC supply activity 43.524 PJ; national power dispatch 41.108 PJ, BC power dispatch 11.700 PJ. This is model context, not a policy target.

| Comparison (2050) | National PJ | BC PJ |
|---|---:|---:|
| OSeCAN supply-activity context | 152.923 | 43.524 |
| Process residue, 50% availability | 257.307 | 90.135 |
| Harvest residue, 60% recovery | 76.716 | 18.006 |

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

Run `.venv/bin/python -m workflows.national.facilities.national_residue_curve_v4` to reproduce the artifact and `.venv/bin/python -m pytest tests/test_national_residue_curve_v4.py -q` to run the regression tests.

No policy/AAC claim is made.
