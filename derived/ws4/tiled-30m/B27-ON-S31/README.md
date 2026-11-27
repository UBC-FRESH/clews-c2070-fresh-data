# WS4 tiled 30-m dataset — B27|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|ON|S31` (parent `B27|ON`)
- Tile / row / col: `B27` / 3 / 1
- Province: `ON`
- Centroid: 45.522045, -74.884169
- Allocated harvest: 6150.152443 m3
- Productive subcell area: 18529.800209 ha
- Committed geometry area: 108666.343470 ha
- Clipped inventory geometry: 108666.343470 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 412695
- Blocks: 143415
- Forest area: 37142.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9865
- Scheduled area: 2706.39 ha
- Eligible blocks (age class >= 40): 98645
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.71 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 5.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
