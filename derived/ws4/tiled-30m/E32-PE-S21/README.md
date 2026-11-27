# WS4 tiled 30-m dataset — E32|PE|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S21` (parent `E32|PE`)
- Tile / row / col: `E32` / 2 / 1
- Province: `PE`
- Centroid: 46.437910, -63.920345
- Allocated harvest: 20930.815112 m3
- Productive subcell area: 19369.386772 ha
- Committed geometry area: 42925.861207 ha
- Clipped inventory geometry: 42925.861207 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 224005
- Blocks: 82463
- Forest area: 20160.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6070
- Scheduled area: 1481.58 ha
- Eligible blocks (age class >= 40): 60692
- Simulated years: 20
- Harvested volume: 193200.717 m3
- Treated/managed area: 1481.580 ha

## Storage

- Dataset: 3.35 MB
- Schedules: 0.07 MB
- Runs: 1.61 MB
- Total: 5.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
