# WS4 tiled 30-m dataset — K1|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S31` (parent `K1|BC`)
- Tile / row / col: `K1` / 3 / 1
- Province: `BC`
- Centroid: 53.641102, -132.813213
- Allocated harvest: 74472.892803 m3
- Productive subcell area: 79324.834584 ha
- Committed geometry area: 84719.533406 ha
- Clipped inventory geometry: 84719.533406 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 901194
- Blocks: 440052
- Forest area: 81107.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43488
- Scheduled area: 7984.62 ha
- Eligible blocks (age class >= 40): 434875
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.59 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 13.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
