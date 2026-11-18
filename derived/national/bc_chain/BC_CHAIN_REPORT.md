# All-BC forest-sector chain at CLEWS B1/B2 zone level

Generated 2026-11-18T07:02:02+00:00.

This is a diagnostic chain, not an operational plan.  It links the 2025 VRI/RSYC area-weighted assortment batch to the 2028 AAC, the FFCM-derived BC facility network through the 2018 NRN road graph, and the Stage B sawmill-residue allocation.  Every proxy is named in the caveats.

## Supply by zone (AAC, area, species/product/residue)

| Zone | Year | AAC m3 | Harvest ha | Log m3 | Gross residue odt | Recoverable odt | Recoverable PJ | Species |
|---|---|---|---|---|---|---|---|---|
| B1 | 2021 | 9,135,921 | 29,030 | 9,135,921 | 331,610 | 198,966 | 3.68 | 22 |
| B2 | 2021 | 40,080,899 | 233,144 | 40,080,899 | 3,964,243 | 2,314,846 | 42.82 | 23 |
| B1 | 2028 | 9,120,805 | 28,982 | 9,120,805 | 331,062 | 198,637 | 3.67 | 22 |
| B2 | 2028 | 34,249,971 | 199,226 | 34,249,971 | 3,387,529 | 1,978,084 | 36.59 | 23 |

Product/species detail is in `bc_supply_by_zone.csv`.  Unmapped species area (SX, S, YC, H, B, ACT, ...) is carried as an explicit `UNMAPPED_BC` row with zero volume and its excluded forest area; it is not redistributed into named species.

## Stage A (assigned/unassigned, utilization, binds, cost, class mix)

Period 2028.  Assigned 45,590,661 m3 of 48,207,935 m3 (94.6%); objective 626,511,267 CAD.

| Zone | Grade | Volume m3 | Delivered CAD/m3 / reason |
|---|---|---|---|
| B1 | OTHER_LOG | 349,601 | 15.00 |
| B1 | PULP | 30 | 15.08 |
| B1 | RESIDUE | 441,416 | 12.18 |
| B1 | SAWLOG | 6,153,900 | 40.03 |
| B2 | OTHER_LOG | 3,957,031 | 8.04 |
| B2 | PULP | 18,112 | 6.29 |
| B2 | RESIDUE | 4,395,743 | 9.97 |
| B2 | SAWLOG | 30,274,828 | 22.72 |
| B1 | SAWLOG | -2,617,273 | unassigned_penalty_exceeds_net_value |

Facility class utilization:

| Class | Facilities | Nameplate m3/y | Assigned m3 | Utilization | Binding |
|---|---|---|---|---|---|
| BIO | 12 | 8,326,259 | 4,320,244 | 51.9% | 3 |
| PAP | 15 | 30,774,260 | 10,127,286 | 32.9% | 5 |
| PEL | 13 | 6,859,300 | 4,841,690 | 70.6% | 7 |
| SAW | 121 | 45,178,430 | 26,301,442 | 58.2% | 38 |

Binding facilities: 53; binding apportionment/nameplate contracts: 34.  Top binding facilities and contracts are in `bc_stage_a_summary.json`.

## Stage B (residue assigned/unassigned, bioenergy share, utilization)

Generated 6,826,610 odt; assigned 6,145,981 odt (90.0%); unassigned 680,629 odt; bioenergy 694,620 odt (10.2% of generated, 11.3% of assigned).

| Residue type | Generated odt | Assigned odt | Unassigned odt |
|---|---|---|---|
| chips | 4,181,691 | 4,050,914 | 130,776 |
| hogfuel | 710,678 | 694,620 | 16,059 |
| other | 500,618 | 0 | 500,618 |
| sawdust_shavings | 1,433,623 | 1,400,447 | 33,176 |

Recipient class utilization:

| Class | Facilities | Capacity odt/y | Received odt | Utilization | Binding |
|---|---|---|---|---|---|
| BIO | 10 | 2,974,911 | 694,620 | 23.3% | 3 |
| PAP | 5 | 4,050,914 | 4,050,914 | 100.0% | 5 |
| PEL | 9 | 2,158,240 | 1,400,447 | 64.9% | 6 |

Stage B net contribution 702,900,181 CAD (revenue - transport - processing).  Full objective decomposition is in `bc_stage_b_summary.json`.

## Comparison to OSeCAN caps

The OSeCAN caps are the 2028+ base residue availability: B1 3.672 PJ/y and B2 39.287 PJ/y.  The comparison below uses the time-path gross taper residue x base recovery fraction, the same basis as the published caps; the scaled batch residue is a second independent check.

| Zone | OSeCAN cap PJ | Batch recoverable PJ | Difference PJ | Difference % |
|---|---|---|---|---|
| B1 | 3.672 | 3.675 | +0.002 | +0.1% |
| B2 | 39.287 | 36.595 | -2.692 | -6.9% |

The batch residue is not a cap calibration: the batch is a per-hectare taper estimate scaled to the same AAC, while OSeCAN is a recovery-adjusted policy cap.  Agreement within a few percent is supportive; disagreement is an evidence gap, not a model target.

## Caveats/tests/commits/publish/status

- **Zone nodes**: area-weighted TSA centroids from dissolved FADM TSA polygons, weighted by 2018 apportionment x THLB share, and restricted to TSAs whose nearest NRN node is in the main road-connected component.  B1 therefore has four weighted TSAs and no island/coastal component node; island and ferry-only facilities are unlinked.  B1 sawlog unassigned volume is an upper bound under this proxy, not evidence that the fibre is uneconomic.
- **Facilities**: FFCM/Mills DB proxies; capacities are normalized processing-line infeed, not licensed or current operating capacity.
- **Contracts**: 2018 apportionment-derived maximum entitlements are diagnostic; min=0 and gate=0 are placeholders, not supply agreements.
- **Unmapped species**: 19.5% of BC forest area (SX etc.) has no RSYC target and is excluded from species composition; the AAC is still allocated across mapped species, so the mapped shares are an assumption.  The excluded area is reported explicitly.
- **Transport**: 2018 NRN road graph shortest paths, road only, no route capacity, no rail/water, and zone centroids can snap several kilometres from the nearest road node.
- **Stage B separation**: Stage A residue assigned to BIO/PEL is a separate harvest-residue allocation; Stage B sawmill residue is derived from Stage A SAW log assignments.  The two models do not share recipient capacity, so their bioenergy totals are additive diagnostics, not one co-optimized balance.
- **Roadside cost**: not modelled; Stage A delivered cost is transport + gate, and processing/revenue come from FFCM lines.

### Tests

- `zone_supply_aac_conservation`: pass
- `zone_supply_recoverable_le_gross`: pass
- `stage_a_mass_balance`: pass
- `stage_a_unit_basis`: pass
- `stage_b_mass_balance`: pass
- `stage_b_validation`: pass

### Reproducibility and status

- Run `make`-free command: `.venv/bin/python -m workflows.national.assignments.bc_chain`.
- Manifest hashes and row counts are in `manifest.json`.
- Parent and `data` submodule commits, annex publication, and `git status --porcelain` are recorded by the operator after the run.
