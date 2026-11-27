# WS4 tiled 30-m dataset — H33|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H33|NL|S13` (parent `H33|NL`)
- Tile / row / col: `H33` / 1 / 3
- Province: `NL`
- Centroid: 48.229828, -58.527989
- Allocated harvest: 8350.796520 m3
- Productive subcell area: 120012.702591 ha
- Committed geometry area: 173429.962048 ha
- Clipped inventory geometry: 173429.962048 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1460457
- Blocks: 630228
- Forest area: 131441.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55877
- Scheduled area: 11355.03 ha
- Eligible blocks (age class >= 40): 558770
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.47 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 20.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
