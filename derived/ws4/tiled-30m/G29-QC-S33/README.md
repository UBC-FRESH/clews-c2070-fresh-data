# WS4 tiled 30-m dataset — G29|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G29|QC|S33` (parent `G29|QC`)
- Tile / row / col: `G29` / 3 / 3
- Province: `QC`
- Centroid: 50.538991, -66.159151
- Allocated harvest: 66610.919039 m3
- Productive subcell area: 201398.701084 ha
- Committed geometry area: 249043.023323 ha
- Clipped inventory geometry: 249043.023323 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2270549
- Blocks: 779999
- Forest area: 204349.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70275
- Scheduled area: 16743.06 ha
- Eligible blocks (age class >= 40): 702748
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.68 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 28.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
