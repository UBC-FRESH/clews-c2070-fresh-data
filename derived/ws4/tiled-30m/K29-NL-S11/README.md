# WS4 tiled 30-m dataset — K29|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S11` (parent `K29|NL`)
- Tile / row / col: `K29` / 1 / 1
- Province: `NL`
- Centroid: 54.898339, -63.789623
- Allocated harvest: 171.662782 m3
- Productive subcell area: 3587.128265 ha
- Committed geometry area: 7616.683575 ha
- Clipped inventory geometry: 7616.683575 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 42269
- Blocks: 28463
- Forest area: 3804.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2497
- Scheduled area: 317.34 ha
- Eligible blocks (age class >= 40): 24964
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.94 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
