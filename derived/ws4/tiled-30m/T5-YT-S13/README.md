# WS4 tiled 30-m dataset — T5|YT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|YT|S13` (parent `T5|YT`)
- Tile / row / col: `T5` / 1 / 3
- Province: `YT`
- Centroid: 66.694115, -135.940403
- Allocated harvest: 216.457718 m3
- Productive subcell area: 131318.209136 ha
- Committed geometry area: 249617.319162 ha
- Clipped inventory geometry: 249617.319162 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1040708
- Blocks: 401209
- Forest area: 93663.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24606
- Scheduled area: 4569.21 ha
- Eligible blocks (age class >= 40): 246052
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.96 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 13.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
