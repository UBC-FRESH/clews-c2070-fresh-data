# WS4 tiled 30-m dataset — D32|NS|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S22` (parent `D32|NS`)
- Tile / row / col: `D32` / 2 / 2
- Province: `NS`
- Centroid: 44.929332, -64.409873
- Allocated harvest: 115988.057988 m3
- Productive subcell area: 200576.148494 ha
- Committed geometry area: 246306.584150 ha
- Clipped inventory geometry: 246306.584150 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2038138
- Blocks: 763197
- Forest area: 183432.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60411
- Scheduled area: 12484.80 ha
- Eligible blocks (age class >= 40): 604107
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.42 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 26.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
