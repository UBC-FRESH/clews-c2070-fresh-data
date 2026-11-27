# WS4 tiled 30-m dataset — G15|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G15|MB|S13` (parent `G15|MB`)
- Tile / row / col: `G15` / 1 / 3
- Province: `MB`
- Centroid: 53.725694, -97.092136
- Allocated harvest: 5714.956909 m3
- Productive subcell area: 162277.652207 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2191575
- Blocks: 881514
- Forest area: 197241.75 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79915
- Scheduled area: 15536.52 ha
- Eligible blocks (age class >= 40): 799150
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.98 MB
- Schedules: 0.95 MB
- Runs: 0.00 MB
- Total: 28.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
