# WS4 tiled 30-m dataset — L29|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L29|NL|S33` (parent `L29|NL`)
- Tile / row / col: `L29` / 3 / 3
- Province: `NL`
- Centroid: 56.423631, -61.047562
- Allocated harvest: 145.391114 m3
- Productive subcell area: 1916.314336 ha
- Committed geometry area: 5040.847338 ha
- Clipped inventory geometry: 5040.847338 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 615
- Blocks: 531
- Forest area: 55.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 99
- Scheduled area: 10.53 ha
- Eligible blocks (age class >= 40): 99
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
