# WS4 tiled 30-m dataset — K31|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S31` (parent `K31|NL`)
- Tile / row / col: `K31` / 3 / 1
- Province: `NL`
- Centroid: 54.426219, -59.203560
- Allocated harvest: 11705.187008 m3
- Productive subcell area: 186825.114590 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1799134
- Blocks: 629823
- Forest area: 161922.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51649
- Scheduled area: 13266.36 ha
- Eligible blocks (age class >= 40): 516486
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.48 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 22.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
