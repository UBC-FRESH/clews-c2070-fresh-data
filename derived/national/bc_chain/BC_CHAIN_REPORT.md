# All-BC forest-sector chain at CLEWS B1/B2 zone level

Generated 2026-11-18T15:16:55+00:00.

This is a diagnostic chain, not an operational plan.  It links the 2025 VRI/RSYC area-weighted assortment batch to the 2028 AAC, the FFCM-derived BC facility network through the 2018 NRN road graph, and the Stage B sawmill-residue allocation.  Every proxy is named in the caveats.

## Supply by zone (AAC, area, species/product/residue)

| Zone | Year | AAC m3 | Harvest ha | Log m3 | Gross residue odt | Recoverable odt | Recoverable PJ | Species |
|---|---|---|---|---|---|---|---|---|
| B1 | 2021 | 9,135,921 | 28,644 | 9,135,921 | 325,356 | 195,214 | 3.61 | 23 |
| B2 | 2021 | 40,080,899 | 226,331 | 40,080,899 | 3,488,670 | 2,037,144 | 37.69 | 24 |
| B1 | 2028 | 9,120,805 | 28,596 | 9,120,805 | 324,818 | 194,891 | 3.61 | 23 |
| B2 | 2028 | 34,249,971 | 193,405 | 34,249,971 | 2,981,142 | 1,740,782 | 32.20 | 24 |

Product/species detail is in `bc_supply_by_zone.csv`.  Documented aliases recover the former SX/S/YC/H/B/ACT/PA gap; residual `UNMAPPED_BC` area is carried as an explicit zero-volume row with its excluded forest area and is not redistributed into named species.

## Stage A (assigned/unassigned, utilization, binds, cost, class mix)

Period 2028.  Assigned 47,672,271 m3 of 47,672,271 m3 (100.0%); objective 3,675,102,299 CAD.

| Zone | Grade | Volume m3 | Delivered CAD/m3 / reason |
|---|---|---|---|
| B1 | OTHER_LOG | 314,439 | 33.39 |
| B1 | PULP | 25 | 35.13 |
| B1 | RESIDUE | 433,090 | 18.06 |
| B1 | SAWLOG | 8,806,340 | 32.71 |
| B2 | OTHER_LOG | 3,159,360 | 34.50 |
| B2 | PULP | 14,044 | 35.70 |
| B2 | RESIDUE | 3,868,405 | 8.00 |
| B2 | SAWLOG | 31,076,566 | 23.74 |

Facility class utilization:

| Class | Facilities | Nameplate m3/y | Assigned m3 | Utilization | Binding |
|---|---|---|---|---|---|
| BIO | 12 | 8,326,259 | 0 | 0.0% | 0 |
| PAP | 15 | 30,774,260 | 14,545,888 | 47.3% | 7 |
| PEL | 13 | 6,859,300 | 4,413,106 | 64.3% | 1 |
| SAW | 121 | 45,178,430 | 28,713,277 | 63.6% | 46 |

Binding facilities: 54; binding apportionment/nameplate contracts: 27.  Top binding facilities and contracts are in `bc_stage_a_summary.json`.

Transport: 298 zone-facility-grade links; 64 use at least one ferry edge.  Ferry cost uses the flagged placeholder 0.03 CAD/m3/km, not a BC Ferries tariff; crossing time is distance / 33 km/h.

## Stage B (residue assigned/unassigned, bioenergy share, utilization)

Generated 7,452,609 odt; assigned 6,856,004 odt (92.0%); unassigned 596,605 odt; bioenergy 758,943 odt (10.2% of generated, 11.1% of assigned).

| Residue type | Generated odt | Assigned odt | Unassigned odt |
|---|---|---|---|
| chips | 4,565,151 | 4,565,151 | 0 |
| hogfuel | 775,847 | 758,943 | 16,904 |
| other | 546,525 | 0 | 546,525 |
| sawdust_shavings | 1,565,086 | 1,531,910 | 33,176 |

Recipient class utilization:

| Class | Facilities | Capacity odt/y | Received odt | Utilization | Binding |
|---|---|---|---|---|---|
| BIO | 10 | 2,974,911 | 758,943 | 25.5% | 3 |
| PAP | 9 | 6,775,713 | 4,565,151 | 67.4% | 5 |
| PEL | 9 | 2,158,240 | 1,531,910 | 71.0% | 6 |

Stage B net contribution 870,128,671 CAD (revenue - transport - processing).  Full objective decomposition is in `bc_stage_b_summary.json`.

## Comparison to OSeCAN caps

The OSeCAN caps are the 2028+ base residue availability: B1 3.672 PJ/y and B2 39.287 PJ/y.  The comparison below uses the time-path gross taper residue x base recovery fraction, the same basis as the published caps; the scaled batch residue is a second independent check.

| Zone | OSeCAN cap PJ | Batch recoverable PJ | Difference PJ | Difference % |
|---|---|---|---|---|
| B1 | 3.672 | 3.605 | -0.067 | -1.8% |
| B2 | 39.287 | 32.204 | -7.082 | -18.0% |

The batch residue is not a cap calibration: the batch is a per-hectare taper estimate scaled to the same AAC, while OSeCAN is a recovery-adjusted policy cap.  Agreement within a few percent is supportive; disagreement is an evidence gap, not a model target.

## Caveats/tests/commits/publish/status

- **Zone nodes**: area-weighted TSA centroids from dissolved FADM TSA polygons, weighted by 2018 apportionment x THLB share, and restricted to TSAs whose nearest NRN node is in the main road-connected component.  With NRN ferry edges, the main component includes Vancouver Island and coastal TSAs where a terminal snapped within the documented tolerance.  Remaining island-only facilities stay unlinked and B1 sawlog unassigned volume is an upper bound under this proxy, not evidence that the fibre is uneconomic.
- **Facilities**: FFCM/Mills DB proxies; capacities are normalized processing-line infeed, not licensed or current operating capacity.
- **Contracts**: 2018 apportionment-derived maximum entitlements are diagnostic; min=0 and gate=0 are placeholders, not supply agreements.
- **Unmapped species**: the area table now applies documented aliases (SX, S, YC, H, B, ACT, PA) with rule and confidence columns.  Any residual `UNMAPPED_BC` area is excluded from species composition and reported explicitly; it is never silently redistributed.
- **Transport**: 2018 NRN road graph plus NRN `FERRYSEG` shortest paths.  Ferry cost uses a flagged placeholder of 0.03 CAD/m3/km, not a BC Ferries tariff; crossing time is distance / 33 km/h.  No route capacity, sailing schedule, queue, or rail/water mode is modelled.
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
