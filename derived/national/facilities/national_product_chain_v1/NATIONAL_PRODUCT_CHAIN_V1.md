# National Product/Residue Chain v1

Generated 2026-11-22T20:21:46+00:00.

This is a coefficient-transfer screening model anchored on the 2028 BC
product/residue chain.  It is not a facility assignment, policy, AAC, or
operating plan.  Every output row is `model_estimate=true`,
`observed=false`, `policy_grade=false`, and `facility_assignment=false`.

## Method

* BC is the only province with a species-resolved product chain.  BC uses
  softwood/hardwood grade shares and class allocations from the 2028 BC
  supply and Stage A assignment.  Class technology ratios come from the BC
  FFCM lines; classes without a group-specific BC line use the aggregate
  donor ratio.
* Every other province receives the BC aggregate donor coefficient and is
  labelled `donor_coefficient`; no provincial yield is fabricated.
* PANEL is absent from BC Stage A.  Its allocation is the explicit BC panel
  nameplate share of sawlog plus panel nameplate, labelled as a BC anchor.
* Harvest residue is gross BC supply with the BC Stage A residue recovery
  share applied.  The recoverable portion is routed to PELLET/BIO; the
  remainder is reported as unrecovered roadside residue.

## Coefficient tiers

| Tier | Scope | Count |
|---|---|---:|
| `bc_anchor_species_group` | coefficient table | 32 |
| `donor_coefficient` | coefficient table | 35 |

## National totals

| Metric | Unit | Value |
|---|---|---:|
| `harvest_m3` | m3 | 118,977,339.100000 |
| `sawlog_m3` | m3 | 109,409,203.971409 |
| `pulpwood_m3` | m3 | 38,597.177183 |
| `other_log_m3` | m3 | 9,529,537.951408 |
| `sawlog_feedstock_m3` | m3 | 70,463,900.791852 |
| `pulp_feedstock_m3` | m3 | 36,672,817.246571 |
| `panel_feedstock_m3` | m3 | 11,534,442.700814 |
| `pellet_feedstock_m3` | m3 | 12,112,415.881686 |
| `bio_feedstock_m3` | m3 | 2,535,764.655785 |
| `residue_feedstock_m3` | m3 | 14,342,002.176707 |
| `total_feedstock_m3` | m3 | 133,319,341.276707 |
| `sawlog_product_m3` | m3 | 48,466,775.661501 |
| `pulp_product_odt` | odt | 7,590,251.823906 |
| `panel_product_m3` | m3 | 5,304,752.545780 |
| `pellet_product_odt` | odt | 4,747,898.211462 |
| `bio_product_mwh` | MWh | 845,182.063302 |
| `process_residue_odt` | odt | 28,432,733.357262 |
| `harvest_residue_gross_odt` | odt | 9,069,108.844605 |
| `harvest_residue_recoverable_odt` | odt | 6,453,900.979518 |
| `harvest_residue_unrecovered_odt` | odt | 2,615,207.865087 |
| `total_residue_gross_odt` | odt | 37,501,842.201867 |
| `total_residue_recoverable_odt` | odt | 34,886,634.336781 |
| `process_residue_odt_per_m3_feedstock` | odt/m3 | 0.213268 |
| `harvest_residue_gross_odt_per_m3_harvest` | odt/m3 | 0.076226 |
| `total_residue_gross_odt_per_m3_harvest` | odt/m3 | 0.315202 |

## Provincial products/residue

| Province | Harvest m3 | SAW feed | PULP feed | PANEL feed | PELLET feed | BIO feed | Process residue odt | Gross harvest residue odt | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| BC | 39,978,577 | 23,677,168 | 12,322,742 | 3,875,785 | 4,069,995 | 852,064 | 9,553,922 | 3,047,388 | `bc_anchor_species_group` |
| AB | 22,891,404 | 13,557,352 | 7,055,901 | 2,219,243 | 2,330,446 | 487,885 | 5,470,497 | 1,744,909 | `donor_coefficient` |
| SK | 4,344,698 | 2,573,132 | 1,339,182 | 421,203 | 442,309 | 92,599 | 1,038,279 | 331,177 | `donor_coefficient` |
| MB | 1,135,236 | 672,339 | 349,918 | 110,057 | 115,572 | 24,195 | 271,294 | 86,534 | `donor_coefficient` |
| ON | 13,493,596 | 7,991,534 | 4,159,180 | 1,308,158 | 1,373,707 | 287,589 | 3,224,646 | 1,028,556 | `donor_coefficient` |
| QC | 26,674,334 | 15,797,778 | 8,221,927 | 2,585,985 | 2,715,564 | 568,510 | 6,374,527 | 2,033,265 | `donor_coefficient` |
| NB | 6,234,700 | 3,692,479 | 1,921,744 | 604,433 | 634,720 | 132,880 | 1,489,944 | 475,243 | `donor_coefficient` |
| NS | 2,388,245 | 1,414,430 | 736,137 | 231,532 | 243,134 | 50,901 | 570,733 | 182,045 | `donor_coefficient` |
| PE | 302,210 | 178,983 | 93,151 | 29,298 | 30,766 | 6,441 | 72,221 | 23,036 | `donor_coefficient` |
| NL | 1,454,038 | 861,148 | 448,183 | 140,964 | 148,027 | 30,990 | 347,480 | 110,835 | `donor_coefficient` |
| YT | 43,926 | 26,015 | 13,539 | 4,258 | 4,472 | 936 | 10,497 | 3,348 | `donor_coefficient` |
| NT | 36,376 | 21,544 | 11,212 | 3,527 | 3,703 | 775 | 8,693 | 2,773 | `donor_coefficient` |
| NU | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | `donor_coefficient` |

## National totals and RSYC comparison

* Model gross harvest residue: **9,069,109 odt**.
* Model recoverable at the RSYC base 0.60 recovery: **5,441,465 odt**.
* RSYC base recoverable residue at the 119 Mm3 provincial harvest: **7,080,062 odt**.
* Ratio: **0.769**.
* Status: **model_below_rsyc**.

The RSYC comparison is a screening check, not a calibration.  BC donor
coefficients are applied to provinces with different species and
residue regimes, so a province-level difference is expected.

## Tests and status

* `finite_values`: **PASS** — 0 non-finite fields
* `nonnegative_values`: **PASS** — 0 negative fields
* `grade_conservation`: **PASS** — failed: []
* `feedstock_conservation`: **PASS** — failed: []
* `residue_total_consistency`: **PASS** — failed: []
* `donor_labels`: **PASS** — failed: []
* `bc_anchor_labels`: **PASS** — failed: []
* `evidence_labels`: **PASS** — failed: []
* `bc_sawmill_residue_crosscheck`: **PASS** — FFCM 0.259552705496 vs Stage B 0.259552705496
* `coefficient_tiers_present`: **PASS** — tiers=['bc_anchor_species_group', 'donor_coefficient']

## Caveats

* No facility assignment, capacity check, transport, cost, or revenue is
  modelled here.  Feedstock and residue are provincial totals only.
* The FFCM archive is a 2018 engineering archive; class ratios are
  technology proxies, not current operating measured yields.
* The BC aggregate donor does not reproduce provincial species mixes.
  Provinces with a large hardwood share may be over-assigned to sawlog.
* BC species-group rows fall back to the BC aggregate ratio where no
  group-specific BC line exists (PANEL/PELLET/BIO and hardwood PULP).
* Harvest residue recovery uses the BC Stage A share; it is not a
  provincial recovery measurement.
* No UI or public OSeCAN surface is changed.

## Reproduce

```bash
.venv/bin/python -m workflows.national.facilities.national_product_chain
```

Status: **pass**.  No policy/AAC claim is made.
