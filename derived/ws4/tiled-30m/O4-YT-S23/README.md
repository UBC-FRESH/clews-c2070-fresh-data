# WS4 tiled 30-m dataset — O4|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|YT|S23` (parent `O4|YT`)
- Tile / row / col: `O4` / 2 / 3
- Province: `YT`
- Centroid: 60.560203, -130.300875
- Allocated harvest: 303.516384 m3
- Productive subcell area: 186577.766324 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2176751
- Blocks: 1058587
- Forest area: 195907.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96782
- Scheduled area: 17080.92 ha
- Eligible blocks (age class >= 40): 967811
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.25 MB
- Schedules: 1.16 MB
- Runs: 0.00 MB
- Total: 31.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
