# WS4 tiled 30-m dataset — G11|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G11|SK|S21` (parent `G11|SK`)
- Tile / row / col: `G11` / 2 / 1
- Province: `SK`
- Centroid: 53.429129, -107.852133
- Allocated harvest: 32819.653730 m3
- Productive subcell area: 139868.653356 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1167590
- Blocks: 460225
- Forest area: 105083.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38213
- Scheduled area: 8828.91 ha
- Eligible blocks (age class >= 40): 382125
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.04 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 15.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
