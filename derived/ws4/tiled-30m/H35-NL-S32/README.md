# WS4 tiled 30-m dataset — H35|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S32` (parent `H35|NL`)
- Tile / row / col: `H35` / 3 / 2
- Province: `NL`
- Centroid: 47.787428, -55.082927
- Allocated harvest: 7171.379685 m3
- Productive subcell area: 96741.641673 ha
- Committed geometry area: 201982.550708 ha
- Clipped inventory geometry: 201982.550708 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 961898
- Blocks: 566815
- Forest area: 86570.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46825
- Scheduled area: 7369.56 ha
- Eligible blocks (age class >= 40): 468249
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.81 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 15.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
