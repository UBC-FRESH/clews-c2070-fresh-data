# WS4 tiled 30-m dataset — N8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N8|NT|S21` (parent `N8|NT`)
- Tile / row / col: `N8` / 2 / 1
- Province: `NT`
- Centroid: 61.458355, -120.524747
- Allocated harvest: 173.224674 m3
- Productive subcell area: 141366.160040 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1951273
- Blocks: 902714
- Forest area: 175614.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79110
- Scheduled area: 14557.41 ha
- Eligible blocks (age class >= 40): 791095
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.31 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 27.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
