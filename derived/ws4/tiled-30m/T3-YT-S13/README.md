# WS4 tiled 30-m dataset — T3|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T3|YT|S13` (parent `T3|YT`)
- Tile / row / col: `T3` / 1 / 3
- Province: `YT`
- Centroid: 64.940336, -140.806563
- Allocated harvest: 43.800754 m3
- Productive subcell area: 27303.494281 ha
- Committed geometry area: 74528.402571 ha
- Clipped inventory geometry: 74528.402571 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 699713
- Blocks: 263110
- Forest area: 62974.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22639
- Scheduled area: 4268.43 ha
- Eligible blocks (age class >= 40): 226387
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.90 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 9.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
