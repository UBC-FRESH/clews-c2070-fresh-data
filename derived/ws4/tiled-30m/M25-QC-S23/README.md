# WS4 tiled 30-m dataset — M25|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M25|QC|S23` (parent `M25|QC`)
- Tile / row / col: `M25` / 2 / 3
- Province: `QC`
- Centroid: 59.819425, -69.677691
- Allocated harvest: 0.430844 m3
- Productive subcell area: 3.366514 ha
- Committed geometry area: 18248.833654 ha
- Clipped inventory geometry: 18248.833654 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 64
- Blocks: 59
- Forest area: 5.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1
- Scheduled area: 0.09 ha
- Eligible blocks (age class >= 40): 1
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.07 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
