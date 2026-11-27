# WS4 tiled 30-m dataset — I23|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I23|QC|S12` (parent `I23|QC`)
- Tile / row / col: `I23` / 1 / 2
- Province: `QC`
- Centroid: 55.042844, -78.278818
- Allocated harvest: 350.182689 m3
- Productive subcell area: 2105.251184 ha
- Committed geometry area: 4390.375256 ha
- Clipped inventory geometry: 4390.375256 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 15623
- Blocks: 8961
- Forest area: 1406.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 594
- Scheduled area: 90.99 ha
- Eligible blocks (age class >= 40): 5940
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.35 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
