# WS4 tiled 30-m dataset — T5|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|YT|S11` (parent `T5|YT`)
- Tile / row / col: `T5` / 1 / 1
- Province: `YT`
- Centroid: 66.129266, -137.765992
- Allocated harvest: 216.789563 m3
- Productive subcell area: 131519.529150 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1695174
- Blocks: 434250
- Forest area: 152565.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26501
- Scheduled area: 6437.16 ha
- Eligible blocks (age class >= 40): 265002
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.80 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 18.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
