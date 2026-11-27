# WS4 tiled 30-m dataset — E33|NS|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S12` (parent `E33|NS`)
- Tile / row / col: `E33` / 1 / 2
- Province: `NS`
- Centroid: 45.118408, -62.195869
- Allocated harvest: 78188.393947 m3
- Productive subcell area: 162680.744349 ha
- Committed geometry area: 196226.391913 ha
- Clipped inventory geometry: 196226.391913 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1922108
- Blocks: 671650
- Forest area: 172989.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55617
- Scheduled area: 10781.82 ha
- Eligible blocks (age class >= 40): 556170
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.89 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 23.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
