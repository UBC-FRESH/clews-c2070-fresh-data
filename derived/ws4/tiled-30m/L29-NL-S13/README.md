# WS4 tiled 30-m dataset — L29|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S13` (parent `L29|NL`)
- Tile / row / col: `L29` / 1 / 3
- Province: `NL`
- Centroid: 55.763999, -61.529434
- Allocated harvest: 7052.239474 m3
- Productive subcell area: 92951.400147 ha
- Committed geometry area: 244507.808096 ha
- Clipped inventory geometry: 244507.808096 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1720692
- Blocks: 467057
- Forest area: 154862.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38519
- Scheduled area: 14224.32 ha
- Eligible blocks (age class >= 40): 385183
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.68 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 19.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
