# WS4 tiled 30-m dataset — F22|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F22|ON|S13` (parent `F22|ON`)
- Tile / row / col: `F22` / 1 / 3
- Province: `ON`
- Centroid: 51.502983, -81.618159
- Allocated harvest: 8693.147078 m3
- Productive subcell area: 131026.727169 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1089241
- Blocks: 423715
- Forest area: 98031.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37270
- Scheduled area: 8427.78 ha
- Eligible blocks (age class >= 40): 372695
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.79 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 14.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
