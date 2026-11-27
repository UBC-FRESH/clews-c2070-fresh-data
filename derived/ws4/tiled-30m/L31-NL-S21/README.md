# WS4 tiled 30-m dataset — L31|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S21` (parent `L31|NL`)
- Tile / row / col: `L31` / 2 / 1
- Province: `NL`
- Centroid: 54.995362, -58.275862
- Allocated harvest: 68.128883 m3
- Productive subcell area: 1148.756055 ha
- Committed geometry area: 2066.943909 ha
- Clipped inventory geometry: 2066.943909 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 3444
- Blocks: 2077
- Forest area: 309.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 834
- Scheduled area: 102.42 ha
- Eligible blocks (age class >= 40): 834
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.13 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
