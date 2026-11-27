# WS4 tiled 30-m dataset — H29|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|NL|S31` (parent `H29|NL`)
- Tile / row / col: `H29` / 3 / 1
- Province: `NL`
- Centroid: 52.256299, -66.367912
- Allocated harvest: 1603.089942 m3
- Productive subcell area: 21756.939378 ha
- Committed geometry area: 35805.541450 ha
- Clipped inventory geometry: 35805.541450 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 253099
- Blocks: 110269
- Forest area: 22778.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10075
- Scheduled area: 1970.73 ha
- Eligible blocks (age class >= 40): 100744
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.06 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
