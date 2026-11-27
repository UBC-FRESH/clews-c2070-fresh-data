# WS4 tiled 30-m dataset — F30|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S13` (parent `F30|QC`)
- Tile / row / col: `F30` / 1 / 3
- Province: `QC`
- Centroid: 48.113902, -65.701624
- Allocated harvest: 7559.532145 m3
- Productive subcell area: 14029.181858 ha
- Committed geometry area: 14851.599693 ha
- Clipped inventory geometry: 14851.599693 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 101127
- Blocks: 49890
- Forest area: 9101.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3968
- Scheduled area: 717.39 ha
- Eligible blocks (age class >= 40): 39672
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.87 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
