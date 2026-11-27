# WS4 tiled 30-m dataset — J29|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|NL|S12` (parent `J29|NL`)
- Tile / row / col: `J29` / 1 / 2
- Province: `NL`
- Centroid: 53.582116, -64.496700
- Allocated harvest: 6509.486467 m3
- Productive subcell area: 139235.398303 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1701149
- Blocks: 631261
- Forest area: 153103.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57698
- Scheduled area: 14565.24 ha
- Eligible blocks (age class >= 40): 576975
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.90 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 21.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
