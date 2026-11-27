# WS4 tiled 30-m dataset — I30|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S13` (parent `I30|QC`)
- Tile / row / col: `I30` / 1 / 3
- Province: `QC`
- Centroid: 51.519729, -62.923101
- Allocated harvest: 43203.253639 m3
- Productive subcell area: 191373.709687 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2278546
- Blocks: 572242
- Forest area: 205069.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53329
- Scheduled area: 19655.91 ha
- Eligible blocks (age class >= 40): 533284
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.37 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 25.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
