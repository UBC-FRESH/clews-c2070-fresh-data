# WS4 tiled 30-m dataset — T4|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S12` (parent `T4|YT`)
- Tile / row / col: `T4` / 1 / 2
- Province: `YT`
- Centroid: 65.543391, -139.511972
- Allocated harvest: 168.824215 m3
- Productive subcell area: 133298.605185 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 935962
- Blocks: 429531
- Forest area: 84236.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28228
- Scheduled area: 4927.05 ha
- Eligible blocks (age class >= 40): 282272
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.74 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 13.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
