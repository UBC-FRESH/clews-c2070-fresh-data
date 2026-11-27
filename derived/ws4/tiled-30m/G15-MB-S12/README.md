# WS4 tiled 30-m dataset — G15|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G15|MB|S12` (parent `G15|MB`)
- Tile / row / col: `G15` / 1 / 2
- Province: `MB`
- Centroid: 53.707930, -97.860912
- Allocated harvest: 5714.956909 m3
- Productive subcell area: 162277.652207 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1278776
- Blocks: 482583
- Forest area: 115089.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46234
- Scheduled area: 11562.03 ha
- Eligible blocks (age class >= 40): 462334
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.47 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 17.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
