# WS4 tiled 30-m dataset — E29|NB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|NB|S12` (parent `E29|NB`)
- Tile / row / col: `E29` / 1 / 2
- Province: `NB`
- Centroid: 47.272445, -68.913716
- Allocated harvest: 21367.747724 m3
- Productive subcell area: 20843.178806 ha
- Committed geometry area: 22315.422891 ha
- Clipped inventory geometry: 22315.422891 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 242827
- Blocks: 72244
- Forest area: 21854.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6114
- Scheduled area: 1623.24 ha
- Eligible blocks (age class >= 40): 61134
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.27 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
