# WS4 tiled 30-m dataset — R2|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S13` (parent `R2|YT`)
- Tile / row / col: `R2` / 1 / 3
- Province: `YT`
- Centroid: 61.930577, -139.473132
- Allocated harvest: 271.575405 m3
- Productive subcell area: 128839.581913 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1929603
- Blocks: 754655
- Forest area: 173664.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60368
- Scheduled area: 11936.34 ha
- Eligible blocks (age class >= 40): 603680
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.09 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 24.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
