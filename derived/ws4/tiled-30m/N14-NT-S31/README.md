# WS4 tiled 30-m dataset — N14|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N14|NT|S31` (parent `N14|NT`)
- Tile / row / col: `N14` / 3 / 1
- Province: `NT`
- Centroid: 64.093451, -103.209433
- Allocated harvest: 0.442958 m3
- Productive subcell area: 925.506153 ha
- Committed geometry area: 231670.492753 ha
- Clipped inventory geometry: 231670.492753 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 23758
- Blocks: 17435
- Forest area: 2138.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2935
- Scheduled area: 340.29 ha
- Eligible blocks (age class >= 40): 2935
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.56 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
