# WS4 tiled 30-m dataset — C19|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C19|ON|S12` (parent `C19|ON`)
- Tile / row / col: `C19` / 1 / 2
- Province: `ON`
- Centroid: 48.213136, -89.529932
- Allocated harvest: 29608.310879 m3
- Productive subcell area: 121325.244684 ha
- Committed geometry area: 145301.326276 ha
- Clipped inventory geometry: 145301.326276 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1397992
- Blocks: 477101
- Forest area: 125819.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42312
- Scheduled area: 10519.74 ha
- Eligible blocks (age class >= 40): 423113
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.15 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 17.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
