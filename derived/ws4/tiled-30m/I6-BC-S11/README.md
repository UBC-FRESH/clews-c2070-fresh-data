# WS4 tiled 30-m dataset — I6|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|BC|S11` (parent `I6|BC`)
- Tile / row / col: `I6` / 1 / 1
- Province: `BC`
- Centroid: 53.584585, -120.085891
- Allocated harvest: 78916.111060 m3
- Productive subcell area: 125856.855094 ha
- Committed geometry area: 166039.929536 ha
- Clipped inventory geometry: 166039.929536 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1179077
- Blocks: 610520
- Forest area: 106116.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57561
- Scheduled area: 9366.30 ha
- Eligible blocks (age class >= 40): 575602
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.03 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 17.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
