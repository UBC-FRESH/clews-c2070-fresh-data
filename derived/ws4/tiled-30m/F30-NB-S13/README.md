# WS4 tiled 30-m dataset — F30|NB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|NB|S13` (parent `F30|NB`)
- Tile / row / col: `F30` / 1 / 3
- Province: `NB`
- Centroid: 47.808658, -65.944885
- Allocated harvest: 78454.437877 m3
- Productive subcell area: 81269.573386 ha
- Committed geometry area: 85816.020813 ha
- Clipped inventory geometry: 85816.020813 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 868317
- Blocks: 294609
- Forest area: 78148.53 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25383
- Scheduled area: 6282.09 ha
- Eligible blocks (age class >= 40): 253823
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.76 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 11.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
