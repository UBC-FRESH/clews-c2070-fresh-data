# WS4 tiled 30-m dataset — D32|NS|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S33` (parent `D32|NS`)
- Tile / row / col: `D32` / 3 / 3
- Province: `NS`
- Centroid: 45.102686, -63.561589
- Allocated harvest: 111382.135643 m3
- Productive subcell area: 192611.206412 ha
- Committed geometry area: 236525.672052 ha
- Clipped inventory geometry: 236525.672052 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2110459
- Blocks: 680700
- Forest area: 189941.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53127
- Scheduled area: 10901.52 ha
- Eligible blocks (age class >= 40): 531264
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.61 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 25.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
