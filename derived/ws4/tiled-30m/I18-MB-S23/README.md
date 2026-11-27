# WS4 tiled 30-m dataset — I18|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S23` (parent `I18|MB`)
- Tile / row / col: `I18` / 2 / 3
- Province: `MB`
- Centroid: 56.790426, -89.757705
- Allocated harvest: 1380.210533 m3
- Productive subcell area: 106650.828749 ha
- Committed geometry area: 198217.545532 ha
- Clipped inventory geometry: 198217.545532 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1218669
- Blocks: 356577
- Forest area: 109680.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27505
- Scheduled area: 10287.18 ha
- Eligible blocks (age class >= 40): 275050
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.00 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 14.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
