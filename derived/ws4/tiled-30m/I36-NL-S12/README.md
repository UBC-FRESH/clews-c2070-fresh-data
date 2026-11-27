# WS4 tiled 30-m dataset — I36|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I36|NL|S12` (parent `I36|NL`)
- Tile / row / col: `I36` / 1 / 2
- Province: `NL`
- Centroid: 47.285989, -53.126059
- Allocated harvest: 12468.299335 m3
- Productive subcell area: 153652.962921 ha
- Committed geometry area: 220966.580029 ha
- Clipped inventory geometry: 220966.580029 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1659513
- Blocks: 825697
- Forest area: 149356.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75500
- Scheduled area: 13432.50 ha
- Eligible blocks (age class >= 40): 754993
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.32 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 24.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
