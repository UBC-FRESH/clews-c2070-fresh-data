# WS4 tiled 30-m dataset — F30|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S12` (parent `F30|QC`)
- Tile / row / col: `F30` / 1 / 2
- Province: `QC`
- Centroid: 48.199279, -66.442864
- Allocated harvest: 78853.176661 m3
- Productive subcell area: 146337.833385 ha
- Committed geometry area: 154916.440838 ha
- Clipped inventory geometry: 154916.440838 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1611660
- Blocks: 509109
- Forest area: 145049.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45001
- Scheduled area: 12357.36 ha
- Eligible blocks (age class >= 40): 450010
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.11 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 19.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
