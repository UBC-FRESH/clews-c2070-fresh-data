# WS4 tiled 30-m dataset — C24|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|QC|S32` (parent `C24|QC`)
- Tile / row / col: `C24` / 3 / 2
- Province: `QC`
- Centroid: 47.919275, -79.262422
- Allocated harvest: 85874.227583 m3
- Productive subcell area: 154085.517469 ha
- Committed geometry area: 195972.509430 ha
- Clipped inventory geometry: 195972.509430 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1780704
- Blocks: 698179
- Forest area: 160263.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63079
- Scheduled area: 13924.62 ha
- Eligible blocks (age class >= 40): 630782
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.00 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 23.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
