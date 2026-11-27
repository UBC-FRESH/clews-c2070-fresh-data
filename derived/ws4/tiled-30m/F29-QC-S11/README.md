# WS4 tiled 30-m dataset — F29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S11` (parent `F29|QC`)
- Tile / row / col: `F29` / 1 / 1
- Province: `QC`
- Centroid: 48.933117, -68.981788
- Allocated harvest: 54508.468856 m3
- Productive subcell area: 118352.940002 ha
- Committed geometry area: 140977.494318 ha
- Clipped inventory geometry: 140977.494318 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1372841
- Blocks: 506068
- Forest area: 123555.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44115
- Scheduled area: 9992.61 ha
- Eligible blocks (age class >= 40): 441144
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.28 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 17.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
