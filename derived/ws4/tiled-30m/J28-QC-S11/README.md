# WS4 tiled 30-m dataset — J28|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|QC|S11` (parent `J28|QC`)
- Tile / row / col: `J28` / 1 / 1
- Province: `QC`
- Centroid: 54.517492, -67.315655
- Allocated harvest: 3061.536775 m3
- Productive subcell area: 21707.982927 ha
- Committed geometry area: 35665.403199 ha
- Clipped inventory geometry: 35665.403199 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 193776
- Blocks: 103210
- Forest area: 17439.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8543
- Scheduled area: 1442.70 ha
- Eligible blocks (age class >= 40): 85421
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.54 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 3.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
