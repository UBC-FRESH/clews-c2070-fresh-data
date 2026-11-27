# WS4 tiled 30-m dataset — L28|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|NL|S12` (parent `L28|NL`)
- Tile / row / col: `L28` / 1 / 2
- Province: `NL`
- Centroid: 56.701938, -63.999269
- Allocated harvest: 113.392577 m3
- Productive subcell area: 2246.735131 ha
- Committed geometry area: 20853.636554 ha
- Clipped inventory geometry: 20853.636554 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1838
- Blocks: 1272
- Forest area: 165.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 180
- Scheduled area: 21.24 ha
- Eligible blocks (age class >= 40): 180
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.11 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
