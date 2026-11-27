# WS4 tiled 30-m dataset — H36|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H36|NL|S33` (parent `H36|NL`)
- Tile / row / col: `H36` / 3 / 3
- Province: `NL`
- Centroid: 46.800132, -53.112204
- Allocated harvest: 2945.962693 m3
- Productive subcell area: 36845.655748 ha
- Committed geometry area: 68632.523391 ha
- Clipped inventory geometry: 68632.523391 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 311047
- Blocks: 161764
- Forest area: 27994.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12455
- Scheduled area: 2202.57 ha
- Eligible blocks (age class >= 40): 124548
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.22 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 5.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
