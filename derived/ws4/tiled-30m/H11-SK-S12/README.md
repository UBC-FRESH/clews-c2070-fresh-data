# WS4 tiled 30-m dataset — H11|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H11|SK|S12` (parent `H11|SK`)
- Tile / row / col: `H11` / 1 / 2
- Province: `SK`
- Centroid: 54.414440, -107.398850
- Allocated harvest: 45593.936486 m3
- Productive subcell area: 190474.751403 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2333250
- Blocks: 760512
- Forest area: 209992.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70922
- Scheduled area: 15874.02 ha
- Eligible blocks (age class >= 40): 709215
- Simulated years: 20
- Harvested volume: 1951362.298 m3
- Treated/managed area: 15874.020 ha

## Storage

- Dataset: 27.18 MB
- Schedules: 0.84 MB
- Runs: 17.29 MB
- Total: 45.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
