# WS4 tiled 30-m dataset — J29|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|NL|S31` (parent `J29|NL`)
- Tile / row / col: `J29` / 3 / 1
- Province: `NL`
- Centroid: 54.557394, -64.489604
- Allocated harvest: 5082.827618 m3
- Productive subcell area: 108719.717203 ha
- Committed geometry area: 195208.471638 ha
- Clipped inventory geometry: 195208.471638 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 983249
- Blocks: 484301
- Forest area: 88492.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42105
- Scheduled area: 7621.92 ha
- Eligible blocks (age class >= 40): 421041
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.79 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 14.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
