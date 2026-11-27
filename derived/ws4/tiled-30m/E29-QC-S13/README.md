# WS4 tiled 30-m dataset — E29|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S13` (parent `E29|QC`)
- Tile / row / col: `E29` / 1 / 3
- Province: `QC`
- Centroid: 47.475550, -68.606635
- Allocated harvest: 11442.204707 m3
- Productive subcell area: 19674.422288 ha
- Committed geometry area: 23872.295569 ha
- Clipped inventory geometry: 23872.295569 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 239315
- Blocks: 77636
- Forest area: 21538.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 6976
- Scheduled area: 1977.21 ha
- Eligible blocks (age class >= 40): 69751
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.35 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
