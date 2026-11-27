# WS4 tiled 30-m dataset — F2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F2|BC|S33` (parent `F2|BC`)
- Tile / row / col: `F2` / 3 / 3
- Province: `BC`
- Centroid: 48.840318, -124.437432
- Allocated harvest: 222150.027897 m3
- Productive subcell area: 231147.891471 ha
- Committed geometry area: 249315.012417 ha
- Clipped inventory geometry: 249315.012417 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2583756
- Blocks: 743013
- Forest area: 232538.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68148
- Scheduled area: 15342.75 ha
- Eligible blocks (age class >= 40): 681477
- Simulated years: 20
- Harvested volume: 5218635.373 m3
- Treated/managed area: 15342.750 ha

## Storage

- Dataset: 28.45 MB
- Schedules: 0.81 MB
- Runs: 16.74 MB
- Total: 46.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
