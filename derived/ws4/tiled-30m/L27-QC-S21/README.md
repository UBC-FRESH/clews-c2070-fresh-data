# WS4 tiled 30-m dataset — L27|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L27|QC|S21` (parent `L27|QC`)
- Tile / row / col: `L27` / 2 / 1
- Province: `QC`
- Centroid: 57.882407, -67.073636
- Allocated harvest: 14919.959864 m3
- Productive subcell area: 91923.631808 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1512666
- Blocks: 788398
- Forest area: 136139.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65456
- Scheduled area: 10712.25 ha
- Eligible blocks (age class >= 40): 654557
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.34 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 22.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
