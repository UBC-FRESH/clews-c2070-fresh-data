# WS4 tiled 30-m dataset — H10|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S13` (parent `H10|SK`)
- Tile / row / col: `H10` / 1 / 3
- Province: `SK`
- Centroid: 54.226586, -108.929227
- Allocated harvest: 47906.369677 m3
- Productive subcell area: 186318.082401 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1371855
- Blocks: 512972
- Forest area: 123466.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42606
- Scheduled area: 10976.85 ha
- Eligible blocks (age class >= 40): 426054
- Simulated years: 20
- Harvested volume: 1555609.410 m3
- Treated/managed area: 10976.850 ha

## Storage

- Dataset: 17.30 MB
- Schedules: 0.50 MB
- Runs: 11.94 MB
- Total: 29.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
