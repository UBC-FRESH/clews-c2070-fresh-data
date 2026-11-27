# WS4 tiled 30-m dataset — L28|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|NL|S13` (parent `L28|NL`)
- Tile / row / col: `L28` / 1 / 3
- Province: `NL`
- Centroid: 56.437673, -63.638679
- Allocated harvest: 1245.229534 m3
- Productive subcell area: 24672.699217 ha
- Committed geometry area: 229005.856183 ha
- Clipped inventory geometry: 229005.856183 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 52862
- Blocks: 30324
- Forest area: 4757.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 771
- Scheduled area: 116.46 ha
- Eligible blocks (age class >= 40): 7705
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.05 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
