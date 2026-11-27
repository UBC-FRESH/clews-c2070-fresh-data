# WS4 tiled 30-m dataset — O4|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O4|BC|S11` (parent `O4|BC`)
- Tile / row / col: `O4` / 1 / 1
- Province: `BC`
- Centroid: 59.676559, -131.371281
- Allocated harvest: 24662.779417 m3
- Productive subcell area: 136404.012166 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1657638
- Blocks: 792024
- Forest area: 149187.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72050
- Scheduled area: 12145.23 ha
- Eligible blocks (age class >= 40): 720500
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.40 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 23.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
