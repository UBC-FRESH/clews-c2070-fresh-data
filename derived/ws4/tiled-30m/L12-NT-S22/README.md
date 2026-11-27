# WS4 tiled 30-m dataset — L12|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S22` (parent `L12|NT`)
- Tile / row / col: `L12` / 2 / 2
- Province: `NT`
- Centroid: 60.546739, -107.000134
- Allocated harvest: 60.433136 m3
- Productive subcell area: 134974.445460 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1433920
- Blocks: 565840
- Forest area: 129052.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46055
- Scheduled area: 9589.41 ha
- Eligible blocks (age class >= 40): 460546
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.25 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 18.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
