# WS4 tiled 30-m dataset — S3|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S3|YT|S33` (parent `S3|YT`)
- Tile / row / col: `S3` / 3 / 3
- Province: `YT`
- Centroid: 64.589978, -140.437872
- Allocated harvest: 451.922852 m3
- Productive subcell area: 186406.753811 ha
- Committed geometry area: 239008.918274 ha
- Clipped inventory geometry: 239008.918274 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2042748
- Blocks: 703650
- Forest area: 183847.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61111
- Scheduled area: 12492.36 ha
- Eligible blocks (age class >= 40): 611109
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.94 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 24.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
