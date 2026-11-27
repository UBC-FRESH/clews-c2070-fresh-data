# WS4 tiled 30-m dataset — D28|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S11` (parent `D28|QC`)
- Tile / row / col: `D28` / 1 / 1
- Province: `QC`
- Centroid: 46.881494, -72.223921
- Allocated harvest: 116138.652827 m3
- Productive subcell area: 198047.763924 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2234044
- Blocks: 676253
- Forest area: 201063.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59406
- Scheduled area: 16332.84 ha
- Eligible blocks (age class >= 40): 594054
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.76 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 26.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
