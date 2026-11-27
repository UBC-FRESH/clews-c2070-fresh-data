# WS4 tiled 30-m dataset — P2|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P2|YT|S13` (parent `P2|YT`)
- Tile / row / col: `P2` / 1 / 3
- Province: `YT`
- Centroid: 60.027575, -135.877758
- Allocated harvest: 5.377043 m3
- Productive subcell area: 2337.752619 ha
- Committed geometry area: 8238.905477 ha
- Clipped inventory geometry: 8238.905477 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 16657
- Blocks: 10411
- Forest area: 1499.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 910
- Scheduled area: 119.61 ha
- Eligible blocks (age class >= 40): 9091
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.40 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
