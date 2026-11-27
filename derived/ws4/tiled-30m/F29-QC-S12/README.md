# WS4 tiled 30-m dataset — F29|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S12` (parent `F29|QC`)
- Tile / row / col: `F29` / 1 / 2
- Province: `QC`
- Centroid: 48.546366, -68.141046
- Allocated harvest: 26860.059049 m3
- Productive subcell area: 58320.606389 ha
- Committed geometry area: 69469.275167 ha
- Clipped inventory geometry: 69469.275167 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 445004
- Blocks: 172891
- Forest area: 40050.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14232
- Scheduled area: 3282.57 ha
- Eligible blocks (age class >= 40): 142319
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.34 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 6.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
