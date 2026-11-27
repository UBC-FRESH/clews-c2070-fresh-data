# WS4 tiled 30-m dataset — K2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S22` (parent `K2|BC`)
- Tile / row / col: `K2` / 2 / 2
- Province: `BC`
- Centroid: 54.265413, -129.961927
- Allocated harvest: 94642.309010 m3
- Productive subcell area: 132732.198287 ha
- Committed geometry area: 188643.255688 ha
- Clipped inventory geometry: 188643.255688 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1689923
- Blocks: 909571
- Forest area: 152093.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88136
- Scheduled area: 14317.29 ha
- Eligible blocks (age class >= 40): 881358
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.22 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 25.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
