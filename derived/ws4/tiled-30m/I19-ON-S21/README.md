# WS4 tiled 30-m dataset — I19|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I19|ON|S21` (parent `I19|ON`)
- Tile / row / col: `I19` / 2 / 1
- Province: `ON`
- Centroid: 56.671093, -88.912630
- Allocated harvest: 2234.268014 m3
- Productive subcell area: 42608.749985 ha
- Committed geometry area: 104058.272803 ha
- Clipped inventory geometry: 104058.272803 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 356508
- Blocks: 116783
- Forest area: 32085.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8700
- Scheduled area: 2588.58 ha
- Eligible blocks (age class >= 40): 86997
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.87 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 4.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
