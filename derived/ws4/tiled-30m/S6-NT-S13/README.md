# WS4 tiled 30-m dataset — S6|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S6|NT|S13` (parent `S6|NT`)
- Tile / row / col: `S6` / 1 / 3
- Province: `NT`
- Centroid: 66.343764, -131.102748
- Allocated harvest: 144.067910 m3
- Productive subcell area: 141156.700007 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1449794
- Blocks: 495208
- Forest area: 130481.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24443
- Scheduled area: 4267.44 ha
- Eligible blocks (age class >= 40): 244421
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.26 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 17.55 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
