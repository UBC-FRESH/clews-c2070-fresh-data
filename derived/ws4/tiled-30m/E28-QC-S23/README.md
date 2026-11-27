# WS4 tiled 30-m dataset — E28|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E28|QC|S23` (parent `E28|QC`)
- Tile / row / col: `E28` / 2 / 3
- Province: `QC`
- Centroid: 48.217712, -70.026691
- Allocated harvest: 103517.305264 m3
- Productive subcell area: 212623.834658 ha
- Committed geometry area: 249999.670247 ha
- Clipped inventory geometry: 249999.670247 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2398225
- Blocks: 873829
- Forest area: 215840.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 82706
- Scheduled area: 19684.71 ha
- Eligible blocks (age class >= 40): 827057
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.84 MB
- Schedules: 0.98 MB
- Runs: 0.00 MB
- Total: 30.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
