# WS4 tiled 30-m dataset — F31|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F31|QC|S11` (parent `F31|QC`)
- Tile / row / col: `F31` / 1 / 1
- Province: `QC`
- Centroid: 48.010183, -65.358837
- Allocated harvest: 317.430983 m3
- Productive subcell area: 636.383024 ha
- Committed geometry area: 678.077226 ha
- Clipped inventory geometry: 678.077226 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2702
- Blocks: 1543
- Forest area: 243.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1056
- Scheduled area: 172.17 ha
- Eligible blocks (age class >= 40): 1056
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.12 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
