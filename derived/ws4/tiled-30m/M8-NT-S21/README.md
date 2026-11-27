# WS4 tiled 30-m dataset — M8|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S21` (parent `M8|NT`)
- Tile / row / col: `M8` / 2 / 1
- Province: `NT`
- Centroid: 60.202680, -119.428610
- Allocated harvest: 138.408824 m3
- Productive subcell area: 99519.831070 ha
- Committed geometry area: 224319.656230 ha
- Clipped inventory geometry: 224319.656230 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1128097
- Blocks: 405218
- Forest area: 101528.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22564
- Scheduled area: 3926.79 ha
- Eligible blocks (age class >= 40): 225633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.73 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 13.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
