# WS4 tiled 30-m dataset — V6|YT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `V6|YT|S12` (parent `V6|YT`)
- Tile / row / col: `V6` / 1 / 2
- Province: `YT`
- Centroid: 69.341041, -138.910419
- Allocated harvest: 3.373278 m3
- Productive subcell area: 2921.782475 ha
- Committed geometry area: 67037.047221 ha
- Clipped inventory geometry: 67037.047221 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 529
- Blocks: 451
- Forest area: 47.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21
- Scheduled area: 2.52 ha
- Eligible blocks (age class >= 40): 21
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
