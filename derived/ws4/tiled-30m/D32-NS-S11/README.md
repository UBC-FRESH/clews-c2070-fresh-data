# WS4 tiled 30-m dataset — D32|NS|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S11` (parent `D32|NS`)
- Tile / row / col: `D32` / 1 / 1
- Province: `NS`
- Centroid: 44.721862, -65.230138
- Allocated harvest: 106768.693350 m3
- Productive subcell area: 184633.260213 ha
- Committed geometry area: 226728.790960 ha
- Clipped inventory geometry: 226728.790960 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2136910
- Blocks: 796962
- Forest area: 192321.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66801
- Scheduled area: 14157.18 ha
- Eligible blocks (age class >= 40): 668006
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.75 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 27.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
