# WS4 tiled 30-m dataset — T4|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S33` (parent `T4|YT`)
- Tile / row / col: `T4` / 3 / 3
- Province: `YT`
- Centroid: 66.547263, -140.118802
- Allocated harvest: 168.824215 m3
- Productive subcell area: 133298.605185 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1767653
- Blocks: 604075
- Forest area: 159088.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46803
- Scheduled area: 11449.80 ha
- Eligible blocks (age class >= 40): 468029
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.11 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 21.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
