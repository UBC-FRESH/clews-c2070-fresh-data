# WS4 tiled 30-m dataset — K16|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K16|MB|S23` (parent `K16|MB`)
- Tile / row / col: `K16` / 2 / 3
- Province: `MB`
- Centroid: 59.715223, -95.004683
- Allocated harvest: 330.634199 m3
- Productive subcell area: 17877.731058 ha
- Committed geometry area: 106306.428565 ha
- Clipped inventory geometry: 106306.428565 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2837
- Blocks: 2511
- Forest area: 255.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 875
- Scheduled area: 84.96 ha
- Eligible blocks (age class >= 40): 875
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.14 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
