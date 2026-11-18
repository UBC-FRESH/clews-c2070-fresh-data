# BC residue co-optimisation: harvest and sawmill streams over shared capacity

Generated 2026-11-18 for 2028. Diagnostic, not an operating plan.

## Method

- Stage A log assignment is fixed.  Harvest residue is the period-specific recoverable residue offer in `bc_supply_by_zone.csv`, conserved by zone; Stage A-assigned residue is reported separately.
- Sawmill residue is the Stage B FFCM outfeed supply derived from the same Stage A sawlog assignment; `other` remains non-allocatable.
- One LP allocates both streams over facility-level PAP/PEL/BIO capacity, with residue-type eligibility and existing NRN road/ferry links.  It first maximises assigned residue, then maximises net contribution subject to that floor (`service_max_then_profit`).
- Objective basis is identical to Stage B: product revenue minus road transport (CAD/m3 / 0.45 odt/m3) minus FFCM line operating cost.
- Capacity is facility-level, so the two streams cannot double-book a recipient; Stage B line capacities are summed where a facility has more than one line.

## Sources and recipients

| stream | generated odt | assigned odt | unassigned odt | share |
|---|---|---|---|---|
| harvest_residue | 1,935,673 | 1,935,673 | 0 | 100.00% |
| sawmill_residue | 6,906,084 | 6,906,084 | 0 | 100.00% |

### Harvest residue conservation (odt)

| recoverable | Stage A assigned | Stage A unassigned | co-opt assigned | co-opt share of recoverable | co-opt share of Stage A assigned |
|---|---|---|---|---|---|
| 1,935,673 | 1,935,673 | 0 | 1,935,673 | 100.00% | 100.00% |

### Assigned and unassigned by source kind and residue type (odt)

| stream | residue type | generated | assigned | unassigned | assigned share |
|---|---|---|---|---|---|
| harvest_residue | harvest_residue | 1,935,673 | 1,935,673 | 0 | 100.00% |
| sawmill_residue | chips | 4,565,151 | 4,565,151 | 0 | 100.00% |
| sawmill_residue | hogfuel | 775,847 | 775,847 | 0 | 100.00% |
| sawmill_residue | sawdust_shavings | 1,565,086 | 1,565,086 | 0 | 100.00% |

| class | capacity odt/y | received odt | utilization | binding facilities |
|---|---|---|---|---|
| BIO | 2,974,911 | 2,118,366 | 71.21% | 5 |
| PAP | 6,775,713 | 4,565,151 | 67.38% | 6 |
| PEL | 2,158,240 | 2,158,240 | 100.00% | 9 |

## Results

- Assigned: **8,841,757 odt** of 8,841,757 odt generated (100.00%).
- Harvest residue: **1,935,673 odt** of 1,935,673 odt recoverable (100.00%); Stage A had assigned 1,935,673 odt, leaving 0 odt for the co-opt to re-home.
- Bioenergy (BIO class): **2,118,366 odt**, 23.96% of assigned and 23.96% of generated.
- Product revenue: **CAD 2,085,149,286**; transport **CAD 326,876,054**; processing **CAD 811,130,846**.
- Net contribution objective: **CAD 947,142,387** (service_max_then_profit); raw CBC objective CAD 947,142,386.88.
- Separate Stage A+Stage B allocations would claim **8,791,677 odt** at shared recipients and exceed facility capacity by **1,309,343 odt**; the co-optimised solve books that capacity once.

## Comparison to separate Stage B

- Stage B alone assigned **6,856,004 odt** and **758,943 odt** to BIO; the co-opt assigns **8,841,757 odt** and **2,118,366 odt** to BIO.
- Stage B PEL receipts plus the Stage A PEL harvest assignment claim **3,467,583 odt** against **2,158,240 odt** of shared PEL capacity; the co-opt books PEL once at **2,158,240 odt**.
- Route policy: accepted provenance is **real_road_network**. **51** fallback-link pairs were excluded (`non_nrn_fallback`) covering at most **710,678 odt** of source supply; **10** pairs had no transport link and **0** had another unaccepted provenance.

## Recipient utilization

| facility | class | capacity odt/y | received odt | harvest odt | sawmill odt | utilization | binding |
|---|---|---|---|---|---|---|---|
| BC-BIO-4008 | BIO | 6,350 | 6,350 | 0 | 6,350 | 100.00% | yes |
| BC-BIO-4009 | BIO | 17,462 | 17,462 | 0 | 17,462 | 100.00% | yes |
| BC-BIO-4010 | BIO | 331,780 | 106,343 | 0 | 106,343 | 32.05% | no |
| BC-BIO-4011 | BIO | 865,169 | 786,174 | 714,064 | 72,109 | 90.87% | no |
| BC-BIO-4015 | BIO | 152,397 | 152,397 | 0 | 152,397 | 100.00% | yes |
| BC-BIO-4018 | BIO | 273,044 | 273,044 | 247,177 | 25,867 | 100.00% | yes |
| BC-BIO-4022 | BIO | 152,397 | 79,854 | 0 | 79,854 | 52.40% | no |
| BC-BIO-4023 | BIO | 458,778 | 458,778 | 381,278 | 77,500 | 100.00% | yes |
| BC-BIO-4024 | BIO | 458,778 | 237,965 | 0 | 237,965 | 51.87% | no |
| BC-PAP-1163 | PAP | 567,103 | 567,103 | 0 | 567,103 | 100.00% | yes |
| BC-PAP-1319 | PAP | 276,705 | 276,705 | 0 | 276,705 | 100.00% | yes |
| BC-PAP-179 | PAP | 1,267,354 | 1,267,354 | 0 | 1,267,354 | 100.00% | yes |
| BC-PAP-589 | PAP | 1,201,961 | 1,201,961 | 0 | 1,201,961 | 100.00% | yes |
| BC-PAP-590 | PAP | 260,697 | 260,697 | 0 | 260,697 | 100.00% | yes |
| BC-PAP-679 | PAP | 540,441 | 540,441 | 0 | 540,441 | 100.00% | yes |
| BC-PAP-731 | PAP | 960,894 | 450,890 | 0 | 450,890 | 46.92% | no |
| BC-PEL-1141 | PEL | 34,440 | 34,440 | 0 | 34,440 | 100.00% | yes |
| BC-PEL-1650 | PEL | 401,800 | 401,800 | 401,800 | 0 | 100.00% | yes |
| BC-PEL-1652 | PEL | 83,804 | 83,804 | 0 | 83,804 | 100.00% | yes |
| BC-PEL-1653 | PEL | 502,824 | 502,824 | 0 | 502,824 | 100.00% | yes |
| BC-PEL-1654 | PEL | 251,412 | 251,412 | 21,256 | 230,156 | 100.00% | yes |
| BC-PEL-1655 | PEL | 265,188 | 265,188 | 15,589 | 249,599 | 100.00% | yes |
| BC-PEL-1657 | PEL | 251,412 | 251,412 | 0 | 251,412 | 100.00% | yes |
| BC-PEL-1658 | PEL | 229,600 | 229,600 | 154,509 | 75,091 | 100.00% | yes |
| BC-PEL-1659 | PEL | 137,760 | 137,760 | 0 | 137,760 | 100.00% | yes |

## Capacity comparison

| facility | class | capacity | Stage A harvest | Stage B sawmill | separate total | double-booked | co-opt |
|---|---|---|---|---|---|---|---|
| BC-BIO-4008 | BIO | 6,350 | 0 | 6,350 | 6,350 | 0 | 6,350 |
| BC-BIO-4009 | BIO | 17,462 | 0 | 17,462 | 17,462 | 0 | 17,462 |
| BC-BIO-4010 | BIO | 331,780 | 0 | 69,775 | 69,775 | 0 | 106,343 |
| BC-BIO-4011 | BIO | 865,169 | 0 | 72,109 | 72,109 | 0 | 786,174 |
| BC-BIO-4015 | BIO | 152,397 | 0 | 152,397 | 152,397 | 0 | 152,397 |
| BC-BIO-4018 | BIO | 273,044 | 0 | 79,549 | 79,549 | 0 | 273,044 |
| BC-BIO-4022 | BIO | 152,397 | 0 | 79,854 | 79,854 | 0 | 79,854 |
| BC-BIO-4023 | BIO | 458,778 | 0 | 61,099 | 61,099 | 0 | 458,778 |
| BC-BIO-4024 | BIO | 458,778 | 0 | 156,104 | 156,104 | 0 | 237,965 |
| BC-PAP-1163 | PAP | 567,103 | 0 | 567,103 | 567,103 | 0 | 567,103 |
| BC-PAP-1319 | PAP | 276,705 | 0 | 276,705 | 276,705 | 0 | 276,705 |
| BC-PAP-179 | PAP | 1,267,354 | 0 | 1,267,354 | 1,267,354 | 0 | 1,267,354 |
| BC-PAP-589 | PAP | 1,201,961 | 0 | 846,765 | 846,765 | 0 | 1,201,961 |
| BC-PAP-590 | PAP | 260,697 | 0 | 260,697 | 260,697 | 0 | 260,697 |
| BC-PAP-679 | PAP | 540,441 | 0 | 540,441 | 540,441 | 0 | 540,441 |
| BC-PAP-731 | PAP | 960,894 | 0 | 806,086 | 806,086 | 0 | 450,890 |
| BC-PEL-1141 | PEL | 34,440 | 34,440 | 34,440 | 68,880 | 34,440 | 34,440 |
| BC-PEL-1650 | PEL | 401,800 | 401,800 | 401,800 | 803,600 | 401,800 | 401,800 |
| BC-PEL-1652 | PEL | 83,804 | 0 | 83,804 | 83,804 | 0 | 83,804 |
| BC-PEL-1653 | PEL | 502,824 | 502,824 | 76,304 | 579,128 | 76,304 | 502,824 |
| BC-PEL-1654 | PEL | 251,412 | 250,409 | 92,037 | 342,446 | 91,034 | 251,412 |
| BC-PEL-1655 | PEL | 265,188 | 265,188 | 224,752 | 489,940 | 224,752 | 265,188 |
| BC-PEL-1657 | PEL | 251,412 | 251,412 | 251,412 | 502,824 | 251,412 | 251,412 |
| BC-PEL-1658 | PEL | 229,600 | 229,600 | 229,600 | 459,200 | 229,600 | 229,600 |
| BC-PEL-1659 | PEL | 137,760 | 0 | 137,760 | 137,760 | 0 | 137,760 |

## Validation

| check | passed | detail |
|---|---|---|
| source_conservation | yes | all sources assigned <= generated |
| shared_capacity | yes | no recipient exceeds facility-level shared capacity |
| residue_type_eligibility | yes | every allocation matches the declared consumer class |
| transport_link_existence | yes | every allocation uses an accepted, provenance-stamped arc |
| objective_reconciliation | yes | assignment components - raw CBC objective = 0.000000 CAD |
| finite_nonnegative_values | yes | all allocated ODT are finite |

## Gaps and next steps

- Contract maxima are apportionment-derived diagnostic entitlements, not supply agreements; the co-opt uses FFCM facility capacity.
- Stage A harvest residue sends zero ODT to BIO in the baseline.  The co-opt permits BIO because Stage A declares BIO eligible for `RESIDUE`; any positive BIO harvest allocation is a diagnostic reallocation.
- PAP is not eligible for the generic Stage A `RESIDUE` grade, so harvest residue cannot be booked as chips to PAP without a grade/eligibility change; this is the smallest eligibility fix if that option is wanted.
- Sawmill source coordinates are TL-hub proxies or recovered Mills DB points; source-level distances remain the main transport limitation.
- Route capacity, rail/water modes, and moisture blending limits are not modelled; all residue is 0.45 wet-basis.

### Remaining independent-review items (next fix pass)

- Alias-area leakage / `NO_ECOPROVINCE` handling in `workflows/national/assortments/bc_area_weights.py`.
- NaN coercion behaviour in the supply and demand parsers.
- Period alignment between the supply, Stage A, and Stage B tables.
- Stage B validation should become fatal rather than reporting a soft status.
- Add a negative-margin service test at the shared-capacity boundary.
