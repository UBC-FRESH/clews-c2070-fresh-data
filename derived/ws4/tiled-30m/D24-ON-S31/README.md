# WS4 tiled 30-m dataset — D24|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|ON|S31` (parent `D24|ON`)
- Tile / row / col: `D24` / 3 / 1
- Province: `ON`
- Centroid: 49.343759, -79.678672
- Allocated harvest: 21946.023047 m3
- Productive subcell area: 105626.881415 ha
- Committed geometry area: 118075.354828 ha
- Clipped inventory geometry: 118075.354828 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1190150
- Blocks: 453557
- Forest area: 107113.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41958
- Scheduled area: 8914.41 ha
- Eligible blocks (age class >= 40): 419576
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.28 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 15.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
