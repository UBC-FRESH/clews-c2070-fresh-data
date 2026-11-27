# WS4 tiled 30-m dataset — R8|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R8|NT|S22` (parent `R8|NT`)
- Tile / row / col: `R8` / 2 / 2
- Province: `NT`
- Centroid: 66.687754, -124.921623
- Allocated harvest: 54.117985 m3
- Productive subcell area: 151558.072555 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1613504
- Blocks: 442194
- Forest area: 145215.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37567
- Scheduled area: 9923.76 ha
- Eligible blocks (age class >= 40): 375669
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.12 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 17.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
