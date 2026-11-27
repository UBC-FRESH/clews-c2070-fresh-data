# WS4 tiled 30-m dataset — F16|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S21` (parent `F16|MB`)
- Tile / row / col: `F16` / 2 / 1
- Province: `MB`
- Centroid: 52.826481, -96.291491
- Allocated harvest: 7549.432927 m3
- Productive subcell area: 204111.368633 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2203978
- Blocks: 740741
- Forest area: 198358.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62032
- Scheduled area: 13547.97 ha
- Eligible blocks (age class >= 40): 620317
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.08 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 26.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
