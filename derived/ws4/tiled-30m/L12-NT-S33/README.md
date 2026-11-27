# WS4 tiled 30-m dataset — L12|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S33` (parent `L12|NT`)
- Tile / row / col: `L12` / 3 / 3
- Province: `NT`
- Centroid: 61.085072, -106.241687
- Allocated harvest: 60.433136 m3
- Productive subcell area: 134974.445460 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1297108
- Blocks: 527350
- Forest area: 116739.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42583
- Scheduled area: 8891.46 ha
- Eligible blocks (age class >= 40): 425829
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.96 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 17.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
