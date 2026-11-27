# WS4 tiled 30-m dataset — I13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S13` (parent `I13|SK`)
- Tile / row / col: `I13` / 1 / 3
- Province: `SK`
- Centroid: 56.265257, -102.312203
- Allocated harvest: 20441.475233 m3
- Productive subcell area: 127634.152660 ha
- Committed geometry area: 186374.503620 ha
- Clipped inventory geometry: 186374.503620 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1261476
- Blocks: 205202
- Forest area: 113532.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13068
- Scheduled area: 3239.28 ha
- Eligible blocks (age class >= 40): 130671
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.50 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 11.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
