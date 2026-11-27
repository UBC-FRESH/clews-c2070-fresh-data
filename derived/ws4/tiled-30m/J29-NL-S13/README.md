# WS4 tiled 30-m dataset — J29|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|NL|S13` (parent `J29|NL`)
- Tile / row / col: `J29` / 1 / 3
- Province: `NL`
- Centroid: 53.369537, -63.820347
- Allocated harvest: 6509.486467 m3
- Productive subcell area: 139235.398303 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2149026
- Blocks: 575146
- Forest area: 193412.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52903
- Scheduled area: 18178.74 ha
- Eligible blocks (age class >= 40): 529022
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.39 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 24.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
