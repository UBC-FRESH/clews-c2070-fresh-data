# WS4 tiled 30-m dataset — G12|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G12|SK|S21` (parent `G12|SK`)
- Tile / row / col: `G12` / 2 / 1
- Province: `SK`
- Centroid: 53.679954, -105.592758
- Allocated harvest: 32142.591788 m3
- Productive subcell area: 162615.589192 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1788721
- Blocks: 676422
- Forest area: 160984.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60430
- Scheduled area: 12708.72 ha
- Eligible blocks (age class >= 40): 604296
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.33 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 23.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
