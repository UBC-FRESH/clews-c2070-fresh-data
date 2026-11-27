# WS4 tiled 30-m dataset — E29|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E29|QC|S33` (parent `E29|QC`)
- Tile / row / col: `E29` / 3 / 3
- Province: `QC`
- Centroid: 48.143900, -67.930335
- Allocated harvest: 92421.802250 m3
- Productive subcell area: 158915.664656 ha
- Committed geometry area: 192823.029903 ha
- Clipped inventory geometry: 192823.029903 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1954440
- Blocks: 643919
- Forest area: 175899.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52546
- Scheduled area: 13081.50 ha
- Eligible blocks (age class >= 40): 525453
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.95 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 23.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
