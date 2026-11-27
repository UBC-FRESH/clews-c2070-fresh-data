# WS4 tiled 30-m dataset — I29|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S33` (parent `I29|NL`)
- Tile / row / col: `I29` / 3 / 3
- Province: `NL`
- Centroid: 52.973655, -64.178676
- Allocated harvest: 7255.389069 m3
- Productive subcell area: 137152.879098 ha
- Committed geometry area: 243723.744098 ha
- Clipped inventory geometry: 243723.744098 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1731256
- Blocks: 420267
- Forest area: 155813.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37762
- Scheduled area: 12782.43 ha
- Eligible blocks (age class >= 40): 377620
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.08 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 18.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
