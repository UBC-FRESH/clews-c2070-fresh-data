# WS4 tiled 30-m dataset — J33|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S32` (parent `J33|NL`)
- Tile / row / col: `J33` / 3 / 2
- Province: `NL`
- Centroid: 51.441671, -56.013976
- Allocated harvest: 3346.629730 m3
- Productive subcell area: 70699.675675 ha
- Committed geometry area: 106543.206260 ha
- Clipped inventory geometry: 106543.206260 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 586600
- Blocks: 347979
- Forest area: 52794.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31757
- Scheduled area: 4802.76 ha
- Eligible blocks (age class >= 40): 317565
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.49 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 9.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
