# WS4 tiled 30-m dataset — C28|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S11` (parent `C28|QC`)
- Tile / row / col: `C28` / 1 / 1
- Province: `QC`
- Centroid: 45.629637, -72.888520
- Allocated harvest: 73775.091185 m3
- Productive subcell area: 133755.670382 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1116064
- Blocks: 269227
- Forest area: 100445.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16855
- Scheduled area: 5317.56 ha
- Eligible blocks (age class >= 40): 168550
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.81 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 12.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
