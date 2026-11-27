# WS4 tiled 30-m dataset — E30|NB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S23` (parent `E30|NB`)
- Tile / row / col: `E30` / 2 / 3
- Province: `NB`
- Centroid: 47.120151, -66.400156
- Allocated harvest: 250660.199616 m3
- Productive subcell area: 237141.316202 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2698606
- Blocks: 882289
- Forest area: 242874.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67825
- Scheduled area: 13336.47 ha
- Eligible blocks (age class >= 40): 678250
- Simulated years: 20
- Harvested volume: 2407249.524 m3
- Treated/managed area: 13336.470 ha

## Storage

- Dataset: 31.56 MB
- Schedules: 0.81 MB
- Runs: 14.68 MB
- Total: 47.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
