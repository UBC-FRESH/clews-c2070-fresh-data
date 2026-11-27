# WS4 tiled 30-m dataset — G13|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G13|MB|S13` (parent `G13|MB`)
- Tile / row / col: `G13` / 1 / 3
- Province: `MB`
- Centroid: 53.543951, -101.520725
- Allocated harvest: 3949.936129 m3
- Productive subcell area: 83730.363040 ha
- Committed geometry area: 140473.568502 ha
- Clipped inventory geometry: 140473.568502 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1000103
- Blocks: 404855
- Forest area: 90009.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38587
- Scheduled area: 8747.64 ha
- Eligible blocks (age class >= 40): 385865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.09 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 13.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
