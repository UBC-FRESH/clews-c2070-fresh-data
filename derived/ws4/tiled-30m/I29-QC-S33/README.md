# WS4 tiled 30-m dataset — I29|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|QC|S33` (parent `I29|QC`)
- Tile / row / col: `I29` / 3 / 3
- Province: `QC`
- Centroid: 52.705071, -64.052886
- Allocated harvest: 737.831026 m3
- Productive subcell area: 4049.365020 ha
- Committed geometry area: 6276.255902 ha
- Clipped inventory geometry: 6276.255902 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 59665
- Blocks: 12819
- Forest area: 5369.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1239
- Scheduled area: 1134.00 ha
- Eligible blocks (age class >= 40): 12381
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.78 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
