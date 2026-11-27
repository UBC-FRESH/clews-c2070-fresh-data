# WS4 tiled 30-m dataset — L11|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|SK|S22` (parent `L11|SK`)
- Tile / row / col: `L11` / 2 / 2
- Province: `SK`
- Centroid: 59.996478, -109.969789
- Allocated harvest: 20.700957 m3
- Productive subcell area: 179.316282 ha
- Committed geometry area: 285.751131 ha
- Clipped inventory geometry: 285.751131 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2332
- Blocks: 300
- Forest area: 209.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 176
- Scheduled area: 107.55 ha
- Eligible blocks (age class >= 40): 176
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.09 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
