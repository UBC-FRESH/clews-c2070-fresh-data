# WS4 tiled 30-m dataset — H30|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H30|QC|S13` (parent `H30|QC`)
- Tile / row / col: `H30` / 1 / 3
- Province: `QC`
- Centroid: 50.404237, -63.930757
- Allocated harvest: 31135.149659 m3
- Productive subcell area: 125720.559913 ha
- Committed geometry area: 157839.568608 ha
- Clipped inventory geometry: 157839.568608 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1182789
- Blocks: 516036
- Forest area: 106451.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46167
- Scheduled area: 10053.90 ha
- Eligible blocks (age class >= 40): 461666
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.10 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 16.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
