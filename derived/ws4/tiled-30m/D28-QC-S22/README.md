# WS4 tiled 30-m dataset — D28|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S22` (parent `D28|QC`)
- Tile / row / col: `D28` / 2 / 2
- Province: `QC`
- Centroid: 47.139155, -71.381996
- Allocated harvest: 116138.261327 m3
- Productive subcell area: 198047.096310 ha
- Committed geometry area: 249999.157257 ha
- Clipped inventory geometry: 249999.157257 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2541673
- Blocks: 794268
- Forest area: 228750.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72578
- Scheduled area: 19874.88 ha
- Eligible blocks (age class >= 40): 725774
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.67 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 30.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
