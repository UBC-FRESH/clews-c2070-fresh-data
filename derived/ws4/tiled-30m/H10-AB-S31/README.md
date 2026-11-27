# WS4 tiled 30-m dataset — H10|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|AB|S31` (parent `H10|AB`)
- Tile / row / col: `H10` / 3 / 1
- Province: `AB`
- Centroid: 54.904431, -110.825330
- Allocated harvest: 87868.773826 m3
- Productive subcell area: 180737.504911 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2574257
- Blocks: 1027696
- Forest area: 231683.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96188
- Scheduled area: 19187.10 ha
- Eligible blocks (age class >= 40): 961880
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.69 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 33.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
