# WS4 tiled 30-m dataset — K32|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K32|NL|S33` (parent `K32|NL`)
- Tile / row / col: `K32` / 3 / 3
- Province: `NL`
- Centroid: 53.157604, -56.078764
- Allocated harvest: 8280.639050 m3
- Productive subcell area: 150962.512413 ha
- Committed geometry area: 188964.875513 ha
- Clipped inventory geometry: 188964.875513 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1399116
- Blocks: 642341
- Forest area: 125920.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56573
- Scheduled area: 11311.56 ha
- Eligible blocks (age class >= 40): 565730
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.35 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 20.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
