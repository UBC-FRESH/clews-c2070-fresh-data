# WS4 tiled 30-m dataset — E25|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E25|QC|S12` (parent `E25|QC`)
- Tile / row / col: `E25` / 1 / 2
- Province: `QC`
- Centroid: 49.295787, -76.660213
- Allocated harvest: 47773.618433 m3
- Productive subcell area: 170907.680670 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1808240
- Blocks: 663015
- Forest area: 162741.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47764
- Scheduled area: 11015.37 ha
- Eligible blocks (age class >= 40): 477635
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.36 MB
- Schedules: 0.56 MB
- Runs: 0.00 MB
- Total: 22.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
