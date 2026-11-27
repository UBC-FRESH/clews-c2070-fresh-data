# WS4 tiled 30-m dataset — M27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M27|QC|S23` (parent `M27|QC`)
- Tile / row / col: `M27` / 2 / 3
- Province: `QC`
- Centroid: 58.680220, -64.382545
- Allocated harvest: 2762.840786 m3
- Productive subcell area: 15082.333501 ha
- Committed geometry area: 193266.856415 ha
- Clipped inventory geometry: 193266.856415 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 123322
- Blocks: 61530
- Forest area: 11098.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3513
- Scheduled area: 633.87 ha
- Eligible blocks (age class >= 40): 35129
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.24 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
