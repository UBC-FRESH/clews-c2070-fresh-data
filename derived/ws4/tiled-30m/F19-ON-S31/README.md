# WS4 tiled 30-m dataset — F19|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F19|ON|S31` (parent `F19|ON`)
- Tile / row / col: `F19` / 3 / 1
- Province: `ON`
- Centroid: 53.145736, -89.474372
- Allocated harvest: 29832.315511 m3
- Productive subcell area: 204802.351765 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2162956
- Blocks: 636582
- Forest area: 194666.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59105
- Scheduled area: 15159.15 ha
- Eligible blocks (age class >= 40): 591043
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.12 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 24.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
