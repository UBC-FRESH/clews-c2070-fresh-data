# WS4 tiled 30-m dataset — H1|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H1|BC|S13` (parent `H1|BC`)
- Tile / row / col: `H1` / 1 / 3
- Province: `BC`
- Centroid: 50.058476, -127.412887
- Allocated harvest: 3880.774800 m3
- Productive subcell area: 3638.305999 ha
- Committed geometry area: 3808.867750 ha
- Clipped inventory geometry: 3808.867750 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 41409
- Blocks: 14573
- Forest area: 3726.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1439
- Scheduled area: 234.00 ha
- Eligible blocks (age class >= 40): 14387
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.65 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
