# WS4 tiled 30-m dataset — G23|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G23|QC|S13` (parent `G23|QC`)
- Tile / row / col: `G23` / 1 / 3
- Province: `QC`
- Centroid: 52.622179, -78.648673
- Allocated harvest: 2976.562340 m3
- Productive subcell area: 16368.194708 ha
- Committed geometry area: 27080.584293 ha
- Clipped inventory geometry: 27080.584293 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 238356
- Blocks: 113229
- Forest area: 21452.04 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10664
- Scheduled area: 1958.85 ha
- Eligible blocks (age class >= 40): 106633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.05 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 4.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
