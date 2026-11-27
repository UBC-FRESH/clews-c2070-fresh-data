# WS4 tiled 30-m dataset — G2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S22` (parent `G2|BC`)
- Tile / row / col: `G2` / 2 / 2
- Province: `BC`
- Centroid: 49.444217, -125.664407
- Allocated harvest: 220022.803727 m3
- Productive subcell area: 216487.365398 ha
- Committed geometry area: 238252.246706 ha
- Clipped inventory geometry: 238252.246706 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2251493
- Blocks: 1184308
- Forest area: 202634.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 115955
- Scheduled area: 19209.42 ha
- Eligible blocks (age class >= 40): 1159547
- Simulated years: 20
- Harvested volume: 7101623.196 m3
- Treated/managed area: 19209.420 ha

## Storage

- Dataset: 32.31 MB
- Schedules: 1.40 MB
- Runs: 21.32 MB
- Total: 55.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
