# WS4 tiled 30-m dataset — O12|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O12|NT|S32` (parent `O12|NT`)
- Tile / row / col: `O12` / 3 / 2
- Province: `NT`
- Centroid: 64.902814, -109.375624
- Allocated harvest: 0.277999 m3
- Productive subcell area: 595.959973 ha
- Committed geometry area: 29946.889834 ha
- Clipped inventory geometry: 29946.889834 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 11584
- Blocks: 9577
- Forest area: 1042.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3093
- Scheduled area: 295.56 ha
- Eligible blocks (age class >= 40): 3093
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.33 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
