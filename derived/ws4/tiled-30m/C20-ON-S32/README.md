# WS4 tiled 30-m dataset — C20|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C20|ON|S32` (parent `C20|ON`)
- Tile / row / col: `C20` / 3 / 2
- Province: `ON`
- Centroid: 48.957250, -87.277026
- Allocated harvest: 45123.806207 m3
- Productive subcell area: 158409.255225 ha
- Committed geometry area: 187903.287038 ha
- Clipped inventory geometry: 187903.287038 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1887350
- Blocks: 719295
- Forest area: 169861.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68408
- Scheduled area: 14716.17 ha
- Eligible blocks (age class >= 40): 684078
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.74 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 24.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
