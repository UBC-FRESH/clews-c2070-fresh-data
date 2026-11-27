# WS4 tiled 30-m dataset — H3|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S23` (parent `H3|BC`)
- Tile / row / col: `H3` / 2 / 3
- Province: `BC`
- Centroid: 51.463305, -124.109693
- Allocated harvest: 91768.239037 m3
- Productive subcell area: 139257.618241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1731297
- Blocks: 853775
- Forest area: 155816.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80619
- Scheduled area: 13657.95 ha
- Eligible blocks (age class >= 40): 806190
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.15 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 25.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
