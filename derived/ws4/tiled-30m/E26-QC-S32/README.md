# WS4 tiled 30-m dataset — E26|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E26|QC|S32` (parent `E26|QC`)
- Tile / row / col: `E26` / 3 / 2
- Province: `QC`
- Centroid: 49.745993, -74.263024
- Allocated harvest: 63415.489007 m3
- Productive subcell area: 175039.054875 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1845278
- Blocks: 638391
- Forest area: 166075.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50495
- Scheduled area: 10909.26 ha
- Eligible blocks (age class >= 40): 504945
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.30 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 22.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
