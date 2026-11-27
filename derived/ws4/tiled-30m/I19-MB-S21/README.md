# WS4 tiled 30-m dataset — I19|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I19|MB|S21` (parent `I19|MB`)
- Tile / row / col: `I19` / 2 / 1
- Province: `MB`
- Centroid: 56.793177, -89.208213
- Allocated harvest: 153.034241 m3
- Productive subcell area: 11550.476545 ha
- Committed geometry area: 26881.299141 ha
- Clipped inventory geometry: 26881.299141 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 116892
- Blocks: 36735
- Forest area: 10520.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2860
- Scheduled area: 890.73 ha
- Eligible blocks (age class >= 40): 28592
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.74 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
