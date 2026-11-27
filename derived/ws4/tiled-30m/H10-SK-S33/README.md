# WS4 tiled 30-m dataset — H10|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S33` (parent `H10|SK`)
- Tile / row / col: `H10` / 3 / 3
- Province: `SK`
- Centroid: 55.119095, -109.276386
- Allocated harvest: 47906.369677 m3
- Productive subcell area: 186318.082401 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2394442
- Blocks: 609087
- Forest area: 215499.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44265
- Scheduled area: 7341.12 ha
- Eligible blocks (age class >= 40): 442642
- Simulated years: 20
- Harvested volume: 856087.939 m3
- Treated/managed area: 7341.120 ha

## Storage

- Dataset: 24.36 MB
- Schedules: 0.52 MB
- Runs: 8.15 MB
- Total: 33.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
