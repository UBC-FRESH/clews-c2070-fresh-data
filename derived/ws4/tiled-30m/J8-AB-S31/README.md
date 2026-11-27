# WS4 tiled 30-m dataset — J8|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J8|AB|S31` (parent `J8|AB`)
- Tile / row / col: `J8` / 3 / 1
- Province: `AB`
- Centroid: 56.733187, -116.931018
- Allocated harvest: 126368.536618 m3
- Productive subcell area: 212567.530268 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2409686
- Blocks: 879606
- Forest area: 216871.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84459
- Scheduled area: 20191.41 ha
- Eligible blocks (age class >= 40): 844588
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.77 MB
- Schedules: 1.00 MB
- Runs: 0.00 MB
- Total: 30.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
