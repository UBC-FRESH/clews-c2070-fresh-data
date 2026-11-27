# WS4 tiled 30-m dataset — A24|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S21` (parent `A24|ON`)
- Tile / row / col: `A24` / 2 / 1
- Province: `ON`
- Centroid: 44.885607, -81.162442
- Allocated harvest: 7214.656062 m3
- Productive subcell area: 27716.989666 ha
- Committed geometry area: 57767.903817 ha
- Clipped inventory geometry: 57767.903817 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 442442
- Blocks: 130799
- Forest area: 39819.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11144
- Scheduled area: 3344.22 ha
- Eligible blocks (age class >= 40): 111433
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.71 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 5.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
