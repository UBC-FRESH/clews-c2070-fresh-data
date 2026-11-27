# WS4 tiled 30-m dataset — U4|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U4|YT|S13` (parent `U4|YT`)
- Tile / row / col: `U4` / 1 / 3
- Province: `YT`
- Centroid: 66.897698, -140.677610
- Allocated harvest: 188.847895 m3
- Productive subcell area: 105834.207885 ha
- Committed geometry area: 158098.526731 ha
- Clipped inventory geometry: 158098.526731 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1303712
- Blocks: 357672
- Forest area: 117334.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30664
- Scheduled area: 10863.63 ha
- Eligible blocks (age class >= 40): 306638
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.82 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 15.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
