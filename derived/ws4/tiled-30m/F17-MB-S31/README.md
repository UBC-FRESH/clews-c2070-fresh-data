# WS4 tiled 30-m dataset — F17|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F17|MB|S31` (parent `F17|MB`)
- Tile / row / col: `F17` / 3 / 1
- Province: `MB`
- Centroid: 53.442654, -94.279567
- Allocated harvest: 1151.255204 m3
- Productive subcell area: 25630.039830 ha
- Committed geometry area: 29015.885498 ha
- Clipped inventory geometry: 29015.885498 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 313472
- Blocks: 119938
- Forest area: 28212.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11257
- Scheduled area: 2241.99 ha
- Eligible blocks (age class >= 40): 112570
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.66 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 4.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
