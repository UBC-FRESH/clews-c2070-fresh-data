# WS4 tiled 30-m dataset — H34|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H34|NL|S32` (parent `H34|NL`)
- Tile / row / col: `H34` / 3 / 2
- Province: `NL`
- Centroid: 48.525406, -56.732840
- Allocated harvest: 7633.462120 m3
- Productive subcell area: 125945.739779 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1805448
- Blocks: 788674
- Forest area: 162490.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70227
- Scheduled area: 13654.08 ha
- Eligible blocks (age class >= 40): 702268
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.98 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 24.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
