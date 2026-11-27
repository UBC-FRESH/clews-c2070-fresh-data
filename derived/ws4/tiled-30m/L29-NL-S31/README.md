# WS4 tiled 30-m dataset — L29|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S31` (parent `L29|NL`)
- Tile / row / col: `L29` / 3 / 1
- Province: `NL`
- Centroid: 57.019911, -62.135301
- Allocated harvest: 7134.116097 m3
- Productive subcell area: 94030.567520 ha
- Committed geometry area: 247346.548003 ha
- Clipped inventory geometry: 247346.548003 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 845330
- Blocks: 318976
- Forest area: 76079.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23407
- Scheduled area: 5855.31 ha
- Eligible blocks (age class >= 40): 234068
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.86 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 11.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
