# WS4 tiled 30-m dataset — E16|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|ON|S33` (parent `E16|ON`)
- Tile / row / col: `E16` / 3 / 3
- Province: `ON`
- Centroid: 51.924788, -94.789452
- Allocated harvest: 29643.996105 m3
- Productive subcell area: 167604.451554 ha
- Committed geometry area: 247545.227888 ha
- Clipped inventory geometry: 247545.227888 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1819699
- Blocks: 413817
- Forest area: 163772.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25598
- Scheduled area: 12362.67 ha
- Eligible blocks (age class >= 40): 255976
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.24 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 18.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
