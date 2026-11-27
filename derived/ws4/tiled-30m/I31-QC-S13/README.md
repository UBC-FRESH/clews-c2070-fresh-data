# WS4 tiled 30-m dataset — I31|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|QC|S13` (parent `I31|QC`)
- Tile / row / col: `I31` / 1 / 3
- Province: `QC`
- Centroid: 50.845497, -61.045546
- Allocated harvest: 58236.500809 m3
- Productive subcell area: 198644.530764 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1985145
- Blocks: 590676
- Forest area: 178663.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53700
- Scheduled area: 16022.79 ha
- Eligible blocks (age class >= 40): 536992
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.69 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 23.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
