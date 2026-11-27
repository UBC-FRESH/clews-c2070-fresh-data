# WS4 tiled 30-m dataset — J26|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J26|QC|S32` (parent `J26|QC`)
- Tile / row / col: `J26` / 3 / 2
- Province: `QC`
- Centroid: 56.146661, -70.310767
- Allocated harvest: 13507.774698 m3
- Productive subcell area: 127798.873441 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1572712
- Blocks: 690659
- Forest area: 141544.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57025
- Scheduled area: 12078.99 ha
- Eligible blocks (age class >= 40): 570246
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.79 MB
- Schedules: 0.67 MB
- Runs: 0.00 MB
- Total: 21.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
