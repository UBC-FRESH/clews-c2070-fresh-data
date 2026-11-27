# WS4 tiled 30-m dataset — K31|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S21` (parent `K31|NL`)
- Tile / row / col: `K31` / 2 / 1
- Province: `NL`
- Centroid: 54.057448, -59.640449
- Allocated harvest: 10314.588491 m3
- Productive subcell area: 164629.935039 ha
- Committed geometry area: 220299.523702 ha
- Clipped inventory geometry: 220299.523702 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1998857
- Blocks: 532329
- Forest area: 179897.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48290
- Scheduled area: 15344.82 ha
- Eligible blocks (age class >= 40): 482894
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.68 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 22.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
