# WS4 tiled 30-m dataset — C32|NS|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C32|NS|S31` (parent `C32|NS`)
- Tile / row / col: `C32` / 3 / 1
- Province: `NS`
- Centroid: 44.346747, -65.522052
- Allocated harvest: 125092.862101 m3
- Productive subcell area: 208298.587839 ha
- Committed geometry area: 249969.342572 ha
- Clipped inventory geometry: 249969.342572 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2434134
- Blocks: 968652
- Forest area: 219072.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89131
- Scheduled area: 18761.49 ha
- Eligible blocks (age class >= 40): 891308
- Simulated years: 20
- Harvested volume: 3138630.993 m3
- Treated/managed area: 18761.490 ha

## Storage

- Dataset: 31.48 MB
- Schedules: 1.06 MB
- Runs: 20.61 MB
- Total: 53.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
