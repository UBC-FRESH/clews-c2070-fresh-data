# WS4 tiled 30-m dataset — I31|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|QC|S33` (parent `I31|QC`)
- Tile / row / col: `I31` / 3 / 3
- Province: `QC`
- Centroid: 51.622885, -60.303871
- Allocated harvest: 58236.500809 m3
- Productive subcell area: 198644.530764 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2210591
- Blocks: 637923
- Forest area: 198953.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58585
- Scheduled area: 18076.68 ha
- Eligible blocks (age class >= 40): 585842
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.83 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 25.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
