# WS4 tiled 30-m dataset — C17|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C17|ON|S13` (parent `C17|ON`)
- Tile / row / col: `C17` / 1 / 3
- Province: `ON`
- Centroid: 48.474060, -92.552611
- Allocated harvest: 1432.058560 m3
- Productive subcell area: 6490.473956 ha
- Committed geometry area: 8418.252177 ha
- Clipped inventory geometry: 8418.252177 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 79223
- Blocks: 33475
- Forest area: 7130.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3191
- Scheduled area: 702.27 ha
- Eligible blocks (age class >= 40): 31910
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.37 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
