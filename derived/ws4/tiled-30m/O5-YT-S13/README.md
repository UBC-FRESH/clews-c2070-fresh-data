# WS4 tiled 30-m dataset — O5|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|YT|S13` (parent `O5|YT`)
- Tile / row / col: `O5` / 1 / 3
- Province: `YT`
- Centroid: 60.865926, -127.392736
- Allocated harvest: 254.748034 m3
- Productive subcell area: 170279.850663 ha
- Committed geometry area: 246334.951290 ha
- Clipped inventory geometry: 246334.951290 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2374755
- Blocks: 1000202
- Forest area: 213727.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 94008
- Scheduled area: 20964.87 ha
- Eligible blocks (age class >= 40): 940076
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.12 MB
- Schedules: 1.12 MB
- Runs: 0.00 MB
- Total: 32.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
