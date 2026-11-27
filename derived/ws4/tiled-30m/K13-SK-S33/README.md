# WS4 tiled 30-m dataset — K13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S33` (parent `K13|SK`)
- Tile / row / col: `K13` / 3 / 3
- Province: `SK`
- Centroid: 59.847287, -103.034548
- Allocated harvest: 8938.989286 m3
- Productive subcell area: 94455.602374 ha
- Committed geometry area: 166713.668994 ha
- Clipped inventory geometry: 166713.668994 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 974960
- Blocks: 227202
- Forest area: 87746.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16227
- Scheduled area: 5921.73 ha
- Eligible blocks (age class >= 40): 162265
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.89 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 10.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
