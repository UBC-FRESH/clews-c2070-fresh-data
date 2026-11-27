# WS4 tiled 30-m dataset — H6|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S32` (parent `H6|BC`)
- Tile / row / col: `H6` / 3 / 2
- Province: `BC`
- Centroid: 53.177079, -119.199925
- Allocated harvest: 10159.364625 m3
- Productive subcell area: 17225.364550 ha
- Committed geometry area: 28959.067881 ha
- Clipped inventory geometry: 28959.067881 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 64766
- Blocks: 39733
- Forest area: 5828.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3626
- Scheduled area: 538.92 ha
- Eligible blocks (age class >= 40): 36255
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.36 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
