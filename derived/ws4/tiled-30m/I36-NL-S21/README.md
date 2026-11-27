# WS4 tiled 30-m dataset — I36|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I36|NL|S21` (parent `I36|NL`)
- Tile / row / col: `I36` / 2 / 1
- Province: `NL`
- Centroid: 47.878475, -53.223279
- Allocated harvest: 5134.382697 m3
- Productive subcell area: 63273.514129 ha
- Committed geometry area: 90992.921696 ha
- Clipped inventory geometry: 90992.921696 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 707474
- Blocks: 351690
- Forest area: 63672.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31557
- Scheduled area: 5776.74 ha
- Eligible blocks (age class >= 40): 315567
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.32 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 10.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
