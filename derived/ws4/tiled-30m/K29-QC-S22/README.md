# WS4 tiled 30-m dataset — K29|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|QC|S22` (parent `K29|QC`)
- Tile / row / col: `K29` / 2 / 2
- Province: `QC`
- Centroid: 55.228199, -63.433212
- Allocated harvest: 55.324798 m3
- Productive subcell area: 336.019700 ha
- Committed geometry area: 694.430078 ha
- Clipped inventory geometry: 694.430078 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2336
- Blocks: 1225
- Forest area: 210.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 861
- Scheduled area: 133.29 ha
- Eligible blocks (age class >= 40): 861
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.11 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
