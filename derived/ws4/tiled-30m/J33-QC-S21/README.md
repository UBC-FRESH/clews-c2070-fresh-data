# WS4 tiled 30-m dataset — J33|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|QC|S21` (parent `J33|QC`)
- Tile / row / col: `J33` / 2 / 1
- Province: `QC`
- Centroid: 51.551407, -57.213647
- Allocated harvest: 2096.764431 m3
- Productive subcell area: 14345.568734 ha
- Committed geometry area: 40528.267258 ha
- Clipped inventory geometry: 40528.267258 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 122915
- Blocks: 86734
- Forest area: 11062.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5261
- Scheduled area: 639.54 ha
- Eligible blocks (age class >= 40): 52606
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.73 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
