# WS4 tiled 30-m dataset — H10|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S22` (parent `H10|SK`)
- Tile / row / col: `H10` / 2 / 2
- Province: `SK`
- Centroid: 54.572770, -109.743212
- Allocated harvest: 32553.073063 m3
- Productive subcell area: 126605.839478 ha
- Committed geometry area: 169878.626173 ha
- Clipped inventory geometry: 169878.626173 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1455088
- Blocks: 532032
- Forest area: 130957.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49711
- Scheduled area: 11041.65 ha
- Eligible blocks (age class >= 40): 497110
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.18 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 18.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
