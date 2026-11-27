# WS4 tiled 30-m dataset — I17|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I17|MB|S33` (parent `I17|MB`)
- Tile / row / col: `I17` / 3 / 3
- Province: `MB`
- Centroid: 57.356548, -92.545551
- Allocated harvest: 312.610484 m3
- Productive subcell area: 22727.017778 ha
- Committed geometry area: 45714.983040 ha
- Clipped inventory geometry: 45714.983040 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 208632
- Blocks: 95114
- Forest area: 18776.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7124
- Scheduled area: 1502.91 ha
- Eligible blocks (age class >= 40): 71232
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.46 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
