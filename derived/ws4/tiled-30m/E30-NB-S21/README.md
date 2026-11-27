# WS4 tiled 30-m dataset — E30|NB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|NB|S21` (parent `E30|NB`)
- Tile / row / col: `E30` / 2 / 1
- Province: `NB`
- Centroid: 47.500910, -67.588349
- Allocated harvest: 250655.258465 m3
- Productive subcell area: 237136.641542 ha
- Committed geometry area: 249995.071863 ha
- Clipped inventory geometry: 249995.071863 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2494381
- Blocks: 868481
- Forest area: 224494.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66128
- Scheduled area: 14120.73 ha
- Eligible blocks (age class >= 40): 661278
- Simulated years: 20
- Harvested volume: 2861634.120 m3
- Treated/managed area: 14120.730 ha

## Storage

- Dataset: 30.32 MB
- Schedules: 0.78 MB
- Runs: 15.49 MB
- Total: 46.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
