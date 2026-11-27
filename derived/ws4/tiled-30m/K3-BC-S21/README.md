# WS4 tiled 30-m dataset — K3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K3|BC|S21` (parent `K3|BC`)
- Tile / row / col: `K3` / 2 / 1
- Province: `BC`
- Centroid: 54.644231, -128.665121
- Allocated harvest: 110195.225817 m3
- Productive subcell area: 187783.516740 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2022707
- Blocks: 1008287
- Forest area: 182043.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96085
- Scheduled area: 15561.00 ha
- Eligible blocks (age class >= 40): 960843
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.47 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 28.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
