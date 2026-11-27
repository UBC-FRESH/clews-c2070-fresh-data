# WS4 tiled 30-m dataset — H35|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S13` (parent `H35|NL`)
- Tile / row / col: `H35` / 1 / 3
- Province: `NL`
- Centroid: 46.965343, -55.384376
- Allocated harvest: 1158.449952 m3
- Productive subcell area: 15627.446191 ha
- Committed geometry area: 32627.846583 ha
- Clipped inventory geometry: 32627.846583 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 153359
- Blocks: 86349
- Forest area: 13802.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6484
- Scheduled area: 1013.76 ha
- Eligible blocks (age class >= 40): 64836
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.95 MB
- Schedules: 0.07 MB
- Runs: 0.00 MB
- Total: 3.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
