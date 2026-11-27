# WS4 tiled 30-m dataset — E6|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E6|BC|S21` (parent `E6|BC`)
- Tile / row / col: `E6` / 2 / 1
- Province: `BC`
- Centroid: 49.091064, -117.112101
- Allocated harvest: 76786.078714 m3
- Productive subcell area: 83335.021114 ha
- Committed geometry area: 100262.987223 ha
- Clipped inventory geometry: 100262.987223 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 998048
- Blocks: 418731
- Forest area: 89824.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 39109
- Scheduled area: 7160.85 ha
- Eligible blocks (age class >= 40): 391090
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.14 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 13.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
