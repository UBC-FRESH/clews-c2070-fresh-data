# WS4 tiled 30-m dataset — U7|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S22` (parent `U7|NT`)
- Tile / row / col: `U7` / 2 / 2
- Province: `NT`
- Centroid: 69.447198, -134.066194
- Allocated harvest: 4.956407 m3
- Productive subcell area: 4237.291691 ha
- Committed geometry area: 84572.761673 ha
- Clipped inventory geometry: 84572.761673 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 63735
- Blocks: 42620
- Forest area: 5736.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2426
- Scheduled area: 319.95 ha
- Eligible blocks (age class >= 40): 24260
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.38 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
