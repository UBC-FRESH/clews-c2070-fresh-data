# WS4 tiled 30-m dataset — K33|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K33|NL|S31` (parent `K33|NL`)
- Tile / row / col: `K33` / 3 / 1
- Province: `NL`
- Centroid: 52.863207, -55.841363
- Allocated harvest: 85.540879 m3
- Productive subcell area: 1959.332390 ha
- Committed geometry area: 3027.575906 ha
- Clipped inventory geometry: 3027.575906 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 10026
- Blocks: 7068
- Forest area: 902.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4637
- Scheduled area: 614.25 ha
- Eligible blocks (age class >= 40): 4637
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.28 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
