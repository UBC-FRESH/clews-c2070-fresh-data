# WS4 tiled 30-m dataset — F22|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F22|ON|S33` (parent `F22|ON`)
- Tile / row / col: `F22` / 3 / 3
- Province: `ON`
- Centroid: 52.314312, -81.606205
- Allocated harvest: 1344.125372 m3
- Productive subcell area: 20259.216460 ha
- Committed geometry area: 38654.740329 ha
- Clipped inventory geometry: 38654.740329 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 171582
- Blocks: 73691
- Forest area: 15442.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6159
- Scheduled area: 1402.56 ha
- Eligible blocks (age class >= 40): 61581
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.82 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 2.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
