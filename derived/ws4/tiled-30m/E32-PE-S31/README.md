# WS4 tiled 30-m dataset — E32|PE|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S31` (parent `E32|PE`)
- Tile / row / col: `E32` / 3 / 1
- Province: `PE`
- Centroid: 46.609176, -63.925286
- Allocated harvest: 31247.772185 m3
- Productive subcell area: 28916.704006 ha
- Committed geometry area: 64084.342853 ha
- Clipped inventory geometry: 64084.342853 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 372693
- Blocks: 142406
- Forest area: 33542.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10675
- Scheduled area: 2471.94 ha
- Eligible blocks (age class >= 40): 106743
- Simulated years: 20
- Harvested volume: 320461.360 m3
- Treated/managed area: 2471.940 ha

## Storage

- Dataset: 5.43 MB
- Schedules: 0.12 MB
- Runs: 2.70 MB
- Total: 8.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
