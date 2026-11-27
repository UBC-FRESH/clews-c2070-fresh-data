# WS4 tiled 30-m dataset — K1|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S11` (parent `K1|BC`)
- Tile / row / col: `K1` / 1 / 1
- Province: `BC`
- Centroid: 52.877860, -132.043117
- Allocated harvest: 93239.692380 m3
- Productive subcell area: 99314.299423 ha
- Committed geometry area: 106068.435588 ha
- Clipped inventory geometry: 106068.435588 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1107849
- Blocks: 537023
- Forest area: 99706.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52883
- Scheduled area: 8931.15 ha
- Eligible blocks (age class >= 40): 528823
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.26 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 15.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
