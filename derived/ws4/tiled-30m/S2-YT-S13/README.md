# WS4 tiled 30-m dataset — S2|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S2|YT|S13` (parent `S2|YT`)
- Tile / row / col: `S2` / 1 / 3
- Province: `YT`
- Centroid: 62.969916, -140.906938
- Allocated harvest: 42.261536 m3
- Productive subcell area: 15730.980120 ha
- Committed geometry area: 19334.645652 ha
- Clipped inventory geometry: 19334.645652 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 152682
- Blocks: 47433
- Forest area: 13741.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3833
- Scheduled area: 889.65 ha
- Eligible blocks (age class >= 40): 38322
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.16 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
