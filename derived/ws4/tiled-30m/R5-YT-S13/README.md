# WS4 tiled 30-m dataset — R5|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|YT|S13` (parent `R5|YT`)
- Tile / row / col: `R5` / 1 / 3
- Province: `YT`
- Centroid: 64.403150, -132.152897
- Allocated harvest: 75.509136 m3
- Productive subcell area: 67140.154985 ha
- Committed geometry area: 207539.935539 ha
- Clipped inventory geometry: 207539.935539 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 262415
- Blocks: 152485
- Forest area: 23617.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8800
- Scheduled area: 1388.16 ha
- Eligible blocks (age class >= 40): 87993
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.78 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 4.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
