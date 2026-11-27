# WS4 tiled 30-m dataset — H29|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|NL|S33` (parent `H29|NL`)
- Tile / row / col: `H29` / 3 / 3
- Province: `NL`
- Centroid: 51.879354, -65.087944
- Allocated harvest: 3946.074514 m3
- Productive subcell area: 53555.637592 ha
- Committed geometry area: 88136.872946 ha
- Clipped inventory geometry: 88136.872946 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 615151
- Blocks: 284950
- Forest area: 55363.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27116
- Scheduled area: 4613.22 ha
- Eligible blocks (age class >= 40): 271158
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.62 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 8.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
