# WS4 tiled 30-m dataset — E29|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S23` (parent `E29|QC`)
- Tile / row / col: `E29` / 2 / 3
- Province: `QC`
- Centroid: 47.711304, -68.443848
- Allocated harvest: 24677.000614 m3
- Productive subcell area: 42431.134849 ha
- Committed geometry area: 51484.540568 ha
- Clipped inventory geometry: 51484.540568 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 549778
- Blocks: 153884
- Forest area: 49480.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13524
- Scheduled area: 4102.11 ha
- Eligible blocks (age class >= 40): 135235
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.76 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
