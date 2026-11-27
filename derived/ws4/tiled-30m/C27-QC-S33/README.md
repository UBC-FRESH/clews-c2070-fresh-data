# WS4 tiled 30-m dataset — C27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C27|QC|S33` (parent `C27|QC`)
- Tile / row / col: `C27` / 3 / 3
- Province: `QC`
- Centroid: 46.616569, -73.055819
- Allocated harvest: 126873.959371 m3
- Productive subcell area: 213887.146714 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2348987
- Blocks: 714228
- Forest area: 211408.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65375
- Scheduled area: 18214.11 ha
- Eligible blocks (age class >= 40): 653743
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.41 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 28.18 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
