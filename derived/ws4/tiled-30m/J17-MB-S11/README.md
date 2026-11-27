# WS4 tiled 30-m dataset — J17|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J17|MB|S11` (parent `J17|MB`)
- Tile / row / col: `J17` / 1 / 1
- Province: `MB`
- Centroid: 57.867895, -93.892530
- Allocated harvest: 735.699665 m3
- Productive subcell area: 55746.483967 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 237665
- Blocks: 145663
- Forest area: 21389.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9931
- Scheduled area: 1477.08 ha
- Eligible blocks (age class >= 40): 99305
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.53 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
