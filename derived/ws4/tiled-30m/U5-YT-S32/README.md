# WS4 tiled 30-m dataset — U5|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U5|YT|S32` (parent `U5|YT`)
- Tile / row / col: `U5` / 3 / 2
- Province: `YT`
- Centroid: 68.197746, -140.545619
- Allocated harvest: 115.968480 m3
- Productive subcell area: 67154.792859 ha
- Committed geometry area: 205320.247292 ha
- Clipped inventory geometry: 205320.247292 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 473110
- Blocks: 219959
- Forest area: 42579.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16059
- Scheduled area: 3331.98 ha
- Eligible blocks (age class >= 40): 160584
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.96 MB
- Schedules: 0.18 MB
- Runs: 0.00 MB
- Total: 7.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
