# WS4 tiled 30-m dataset — C28|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S12` (parent `C28|QC`)
- Tile / row / col: `C28` / 1 / 2
- Province: `QC`
- Centroid: 45.477829, -72.296824
- Allocated harvest: 73408.405062 m3
- Productive subcell area: 133090.861334 ha
- Committed geometry area: 248757.418944 ha
- Clipped inventory geometry: 248757.418944 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1986698
- Blocks: 575908
- Forest area: 178802.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49230
- Scheduled area: 17181.45 ha
- Eligible blocks (age class >= 40): 492297
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.39 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 22.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
