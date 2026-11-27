# WS4 tiled 30-m dataset — H11|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H11|SK|S13` (parent `H11|SK`)
- Tile / row / col: `H11` / 1 / 3
- Province: `SK`
- Centroid: 54.500285, -106.628059
- Allocated harvest: 45593.936486 m3
- Productive subcell area: 190474.751403 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1520406
- Blocks: 503577
- Forest area: 136836.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43400
- Scheduled area: 8657.01 ha
- Eligible blocks (age class >= 40): 433991
- Simulated years: 20
- Harvested volume: 1093701.618 m3
- Treated/managed area: 8657.010 ha

## Storage

- Dataset: 17.94 MB
- Schedules: 0.51 MB
- Runs: 9.49 MB
- Total: 27.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
