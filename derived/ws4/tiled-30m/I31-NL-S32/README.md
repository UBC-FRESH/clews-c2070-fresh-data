# WS4 tiled 30-m dataset — I31|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|NL|S32` (parent `I31|NL`)
- Tile / row / col: `I31` / 3 / 2
- Province: `NL`
- Centroid: 52.053774, -60.959190
- Allocated harvest: 2862.638660 m3
- Productive subcell area: 33905.500572 ha
- Committed geometry area: 40223.859815 ha
- Clipped inventory geometry: 40223.859815 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 390839
- Blocks: 140324
- Forest area: 35175.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13531
- Scheduled area: 3494.79 ha
- Eligible blocks (age class >= 40): 135307
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.57 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 5.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
