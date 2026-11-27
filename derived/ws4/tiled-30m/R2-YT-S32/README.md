# WS4 tiled 30-m dataset — R2|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S32` (parent `R2|YT`)
- Tile / row / col: `R2` / 3 / 2
- Province: `YT`
- Centroid: 62.313448, -140.937958
- Allocated harvest: 9.762413 m3
- Productive subcell area: 4631.440020 ha
- Committed geometry area: 8986.834541 ha
- Clipped inventory geometry: 8986.834541 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 56262
- Blocks: 24162
- Forest area: 5063.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1778
- Scheduled area: 286.65 ha
- Eligible blocks (age class >= 40): 17778
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.99 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
