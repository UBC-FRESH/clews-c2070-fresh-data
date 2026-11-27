# WS4 tiled 30-m dataset — G3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S21` (parent `G3|BC`)
- Tile / row / col: `G3` / 2 / 1
- Province: `BC`
- Centroid: 49.895161, -124.371706
- Allocated harvest: 95936.978216 m3
- Productive subcell area: 109960.384909 ha
- Committed geometry area: 154749.460180 ha
- Clipped inventory geometry: 154749.460180 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1428656
- Blocks: 612068
- Forest area: 128579.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57085
- Scheduled area: 9507.33 ha
- Eligible blocks (age class >= 40): 570848
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.01 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 19.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
