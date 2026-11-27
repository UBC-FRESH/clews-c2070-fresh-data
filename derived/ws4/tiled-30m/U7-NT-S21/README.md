# WS4 tiled 30-m dataset — U7|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S21` (parent `U7|NT`)
- Tile / row / col: `U7` / 2 / 1
- Province: `NT`
- Centroid: 69.246644, -134.870916
- Allocated harvest: 12.525552 m3
- Productive subcell area: 10708.244887 ha
- Committed geometry area: 213727.519546 ha
- Clipped inventory geometry: 213727.519546 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 277062
- Blocks: 161695
- Forest area: 24935.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7808
- Scheduled area: 984.24 ha
- Eligible blocks (age class >= 40): 78075
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.97 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 5.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
