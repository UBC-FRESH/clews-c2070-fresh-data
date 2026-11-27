# WS4 tiled 30-m dataset — V5|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V5|YT|S12` (parent `V5|YT`)
- Tile / row / col: `V5` / 1 / 2
- Province: `YT`
- Centroid: 68.537281, -140.875504
- Allocated harvest: 3.634952 m3
- Productive subcell area: 3706.847003 ha
- Committed geometry area: 27133.081152 ha
- Clipped inventory geometry: 27133.081152 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 120996
- Blocks: 33976
- Forest area: 10889.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1958
- Scheduled area: 471.51 ha
- Eligible blocks (age class >= 40): 19575
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.70 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
