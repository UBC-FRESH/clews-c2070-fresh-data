# WS4 tiled 30-m dataset — D28|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S21` (parent `D28|QC`)
- Tile / row / col: `D28` / 2 / 1
- Province: `QC`
- Centroid: 47.299158, -71.993814
- Allocated harvest: 116138.652827 m3
- Productive subcell area: 198047.763924 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2534973
- Blocks: 897157
- Forest area: 228147.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 82918
- Scheduled area: 19376.46 ha
- Eligible blocks (age class >= 40): 829174
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.98 MB
- Schedules: 0.98 MB
- Runs: 0.00 MB
- Total: 31.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
