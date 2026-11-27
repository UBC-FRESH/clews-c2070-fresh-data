# WS4 tiled 30-m dataset — K33|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K33|NL|S12` (parent `K33|NL`)
- Tile / row / col: `K33` / 1 / 2
- Province: `NL`
- Centroid: 51.950325, -55.355109
- Allocated harvest: 883.815339 m3
- Productive subcell area: 20243.982134 ha
- Committed geometry area: 31281.161312 ha
- Clipped inventory geometry: 31281.161312 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 131403
- Blocks: 72647
- Forest area: 11826.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5621
- Scheduled area: 953.37 ha
- Eligible blocks (age class >= 40): 56201
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.55 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
