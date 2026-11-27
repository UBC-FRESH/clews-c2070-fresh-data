# WS4 tiled 30-m dataset — H33|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H33|NL|S33` (parent `H33|NL`)
- Tile / row / col: `H33` / 3 / 3
- Province: `NL`
- Centroid: 49.021857, -57.845560
- Allocated harvest: 11200.040863 m3
- Productive subcell area: 160960.355082 ha
- Committed geometry area: 232603.280072 ha
- Clipped inventory geometry: 232603.280072 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2031975
- Blocks: 889861
- Forest area: 182877.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 82919
- Scheduled area: 14754.24 ha
- Eligible blocks (age class >= 40): 829184
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.68 MB
- Schedules: 0.98 MB
- Runs: 0.00 MB
- Total: 27.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
