# WS4 tiled 30-m dataset — F16|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F16|MB|S33` (parent `F16|MB`)
- Tile / row / col: `F16` / 3 / 3
- Province: `MB`
- Centroid: 53.312421, -94.823596
- Allocated harvest: 6557.202708 m3
- Productive subcell area: 177284.788426 ha
- Committed geometry area: 217142.226832 ha
- Clipped inventory geometry: 217142.226832 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2215345
- Blocks: 829879
- Forest area: 199381.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79270
- Scheduled area: 16785.81 ha
- Eligible blocks (age class >= 40): 792691
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.48 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 28.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
