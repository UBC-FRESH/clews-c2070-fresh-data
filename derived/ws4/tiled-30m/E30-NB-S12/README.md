# WS4 tiled 30-m dataset — E30|NB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S12` (parent `E30|NB`)
- Tile / row / col: `E30` / 1 / 2
- Province: `NB`
- Centroid: 46.908211, -67.268986
- Allocated harvest: 250660.199616 m3
- Productive subcell area: 237141.316202 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2597813
- Blocks: 939888
- Forest area: 233803.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74687
- Scheduled area: 14721.66 ha
- Eligible blocks (age class >= 40): 746869
- Simulated years: 20
- Harvested volume: 2883743.661 m3
- Treated/managed area: 14721.660 ha

## Storage

- Dataset: 31.77 MB
- Schedules: 0.89 MB
- Runs: 16.21 MB
- Total: 48.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
