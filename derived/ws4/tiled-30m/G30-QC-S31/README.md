# WS4 tiled 30-m dataset — G30|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G30|QC|S31` (parent `G30|QC`)
- Tile / row / col: `G30` / 3 / 1
- Province: `QC`
- Centroid: 50.416001, -65.523767
- Allocated harvest: 62215.077102 m3
- Productive subcell area: 140229.228209 ha
- Committed geometry area: 160908.043099 ha
- Clipped inventory geometry: 160908.043099 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1602031
- Blocks: 565827
- Forest area: 144182.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53598
- Scheduled area: 14032.17 ha
- Eligible blocks (age class >= 40): 535978
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.87 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 20.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
