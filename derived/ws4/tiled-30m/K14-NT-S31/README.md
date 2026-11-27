# WS4 tiled 30-m dataset — K14|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|NT|S31` (parent `K14|NT`)
- Tile / row / col: `K14` / 3 / 1
- Province: `NT`
- Centroid: 60.101719, -102.299107
- Allocated harvest: 16.699398 m3
- Productive subcell area: 34697.230556 ha
- Committed geometry area: 72350.917632 ha
- Clipped inventory geometry: 72350.917632 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 395227
- Blocks: 84854
- Forest area: 35570.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7272
- Scheduled area: 2332.89 ha
- Eligible blocks (age class >= 40): 72720
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.30 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 4.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
