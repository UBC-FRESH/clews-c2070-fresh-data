# WS4 tiled 30-m dataset — I14|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I14|MB|S23` (parent `I14|MB`)
- Tile / row / col: `I14` / 2 / 3
- Province: `MB`
- Centroid: 56.853712, -99.801212
- Allocated harvest: 6068.554782 m3
- Productive subcell area: 182529.009153 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2023199
- Blocks: 355600
- Forest area: 182087.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26063
- Scheduled area: 8631.99 ha
- Eligible blocks (age class >= 40): 260621
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.76 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 19.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
