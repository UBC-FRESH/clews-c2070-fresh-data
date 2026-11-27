# WS4 tiled 30-m dataset — I36|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I36|NL|S22` (parent `I36|NL`)
- Tile / row / col: `I36` / 2 / 2
- Province: `NL`
- Centroid: 47.575833, -52.789552
- Allocated harvest: 3591.658493 m3
- Productive subcell area: 44261.767737 ha
- Committed geometry area: 63652.345238 ha
- Clipped inventory geometry: 63652.345238 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 462487
- Blocks: 198739
- Forest area: 41623.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17781
- Scheduled area: 3925.53 ha
- Eligible blocks (age class >= 40): 177803
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.74 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 6.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
