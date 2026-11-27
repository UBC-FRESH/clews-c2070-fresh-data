# WS4 tiled 30-m dataset — I5|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I5|BC|S12` (parent `I5|BC`)
- Tile / row / col: `I5` / 1 / 2
- Province: `BC`
- Centroid: 53.248105, -121.371839
- Allocated harvest: 167830.547591 m3
- Productive subcell area: 208161.988726 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2441836
- Blocks: 902558
- Forest area: 219765.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84761
- Scheduled area: 19946.25 ha
- Eligible blocks (age class >= 40): 847609
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.15 MB
- Schedules: 1.01 MB
- Runs: 0.00 MB
- Total: 31.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
