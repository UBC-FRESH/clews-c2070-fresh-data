# WS4 tiled 30-m dataset — K32|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S22` (parent `K32|NL`)
- Tile / row / col: `K32` / 2 / 2
- Province: `NL`
- Centroid: 53.044228, -57.049263
- Allocated harvest: 10955.262225 m3
- Productive subcell area: 199722.980268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2395906
- Blocks: 755194
- Forest area: 215631.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70662
- Scheduled area: 19116.63 ha
- Eligible blocks (age class >= 40): 706620
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.67 MB
- Schedules: 0.84 MB
- Runs: 0.00 MB
- Total: 28.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
