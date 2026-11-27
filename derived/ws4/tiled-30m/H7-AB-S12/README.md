# WS4 tiled 30-m dataset — H7|AB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H7|AB|S12` (parent `H7|AB`)
- Tile / row / col: `H7` / 1 / 2
- Province: `AB`
- Centroid: 52.976782, -116.310978
- Allocated harvest: 197916.560201 m3
- Productive subcell area: 219705.769105 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2604623
- Blocks: 906325
- Forest area: 234416.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71852
- Scheduled area: 13314.69 ha
- Eligible blocks (age class >= 40): 718517
- Simulated years: 20
- Harvested volume: 3814738.695 m3
- Treated/managed area: 13314.690 ha

## Storage

- Dataset: 30.83 MB
- Schedules: 0.85 MB
- Runs: 14.71 MB
- Total: 46.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
