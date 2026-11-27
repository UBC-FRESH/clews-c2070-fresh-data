# WS4 tiled 30-m dataset — K31|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S33` (parent `K31|NL`)
- Tile / row / col: `K31` / 3 / 3
- Province: `NL`
- Centroid: 53.924026, -57.891452
- Allocated harvest: 11287.593935 m3
- Productive subcell area: 180159.960617 ha
- Committed geometry area: 241081.025177 ha
- Clipped inventory geometry: 241081.025177 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2112463
- Blocks: 807346
- Forest area: 190121.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72914
- Scheduled area: 17446.59 ha
- Eligible blocks (age class >= 40): 729134
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.19 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 27.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
