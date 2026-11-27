# WS4 tiled 30-m dataset — M7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M7|BC|S11` (parent `M7|BC`)
- Tile / row / col: `M7` / 1 / 1
- Province: `BC`
- Centroid: 59.211875, -121.603619
- Allocated harvest: 72421.782174 m3
- Productive subcell area: 178443.689183 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1832699
- Blocks: 745825
- Forest area: 164942.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59603
- Scheduled area: 11452.05 ha
- Eligible blocks (age class >= 40): 596030
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.32 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 24.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
