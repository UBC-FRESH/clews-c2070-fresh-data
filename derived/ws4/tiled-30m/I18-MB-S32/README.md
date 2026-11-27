# WS4 tiled 30-m dataset — I18|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I18|MB|S32` (parent `I18|MB`)
- Tile / row / col: `I18` / 3 / 2
- Province: `MB`
- Centroid: 57.162762, -90.653533
- Allocated harvest: 355.648139 m3
- Productive subcell area: 27481.436971 ha
- Committed geometry area: 51076.049272 ha
- Clipped inventory geometry: 51076.049272 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 237111
- Blocks: 71181
- Forest area: 21339.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5522
- Scheduled area: 1426.77 ha
- Eligible blocks (age class >= 40): 55216
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.12 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
