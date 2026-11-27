# WS4 tiled 30-m dataset — I23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I23|QC|S33` (parent `I23|QC`)
- Tile / row / col: `I23` / 3 / 3
- Province: `QC`
- Centroid: 55.769302, -77.046853
- Allocated harvest: 6.494574 m3
- Productive subcell area: 39.044506 ha
- Committed geometry area: 81.424979 ha
- Clipped inventory geometry: 81.424979 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 125
- Blocks: 84
- Forest area: 11.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42
- Scheduled area: 6.48 ha
- Eligible blocks (age class >= 40): 42
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
