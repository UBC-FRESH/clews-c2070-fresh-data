# WS4 tiled 30-m dataset — F16|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S11` (parent `F16|MB`)
- Tile / row / col: `F16` / 1 / 1
- Province: `MB`
- Centroid: 52.371615, -96.276409
- Allocated harvest: 7549.432927 m3
- Productive subcell area: 204111.368633 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1995360
- Blocks: 703299
- Forest area: 179582.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47446
- Scheduled area: 8663.76 ha
- Eligible blocks (age class >= 40): 474460
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.48 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 24.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
