# WS4 tiled 30-m dataset — I11|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I11|SK|S33` (parent `I11|SK`)
- Tile / row / col: `I11` / 3 / 3
- Province: `SK`
- Centroid: 56.751723, -107.388343
- Allocated harvest: 28220.710290 m3
- Productive subcell area: 170588.489849 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2032298
- Blocks: 281582
- Forest area: 182906.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17652
- Scheduled area: 5640.21 ha
- Eligible blocks (age class >= 40): 176520
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.38 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 16.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
