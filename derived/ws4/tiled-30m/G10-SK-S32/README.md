# WS4 tiled 30-m dataset — G10|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|SK|S32` (parent `G10|SK`)
- Tile / row / col: `G10` / 3 / 2
- Province: `SK`
- Centroid: 53.680061, -109.512507
- Allocated harvest: 21047.038587 m3
- Productive subcell area: 87530.582817 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1330745
- Blocks: 471023
- Forest area: 119767.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38775
- Scheduled area: 10303.83 ha
- Eligible blocks (age class >= 40): 387746
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.68 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 17.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
