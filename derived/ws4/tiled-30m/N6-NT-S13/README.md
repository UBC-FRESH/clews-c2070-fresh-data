# WS4 tiled 30-m dataset — N6|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|NT|S13` (parent `N6|NT`)
- Tile / row / col: `N6` / 1 / 3
- Province: `NT`
- Centroid: 60.277067, -123.584793
- Allocated harvest: 287.829176 m3
- Productive subcell area: 195619.993808 ha
- Committed geometry area: 247631.162126 ha
- Clipped inventory geometry: 247631.162126 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2590695
- Blocks: 1184250
- Forest area: 233162.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 116679
- Scheduled area: 22135.41 ha
- Eligible blocks (age class >= 40): 1166784
- Simulated years: 20
- Harvested volume: 3216356.009 m3
- Treated/managed area: 22135.410 ha

## Storage

- Dataset: 35.43 MB
- Schedules: 1.41 MB
- Runs: 24.39 MB
- Total: 61.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
