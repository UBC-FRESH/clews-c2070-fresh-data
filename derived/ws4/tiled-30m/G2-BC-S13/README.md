# WS4 tiled 30-m dataset — G2|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S13` (parent `G2|BC`)
- Tile / row / col: `G2` / 1 / 3
- Province: `BC`
- Centroid: 49.226921, -124.754699
- Allocated harvest: 209452.931415 m3
- Productive subcell area: 206087.335171 ha
- Committed geometry area: 226806.633874 ha
- Clipped inventory geometry: 226806.633874 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2249358
- Blocks: 742968
- Forest area: 202442.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68137
- Scheduled area: 12959.64 ha
- Eligible blocks (age class >= 40): 681363
- Simulated years: 20
- Harvested volume: 4895282.001 m3
- Treated/managed area: 12959.640 ha

## Storage

- Dataset: 26.03 MB
- Schedules: 0.81 MB
- Runs: 14.26 MB
- Total: 41.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
