# WS4 tiled 30-m dataset — J3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J3|BC|S11` (parent `J3|BC`)
- Tile / row / col: `J3` / 1 / 1
- Province: `BC`
- Centroid: 53.057657, -127.138195
- Allocated harvest: 79718.457351 m3
- Productive subcell area: 186223.493251 ha
- Committed geometry area: 249147.652154 ha
- Clipped inventory geometry: 249147.652154 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1438846
- Blocks: 849565
- Forest area: 129496.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79932
- Scheduled area: 11941.92 ha
- Eligible blocks (age class >= 40): 799316
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.69 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 22.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
