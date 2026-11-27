# WS4 tiled 30-m dataset — C26|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S23` (parent `C26|QC`)
- Tile / row / col: `C26` / 2 / 3
- Province: `QC`
- Centroid: 46.626684, -75.100006
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2354560
- Blocks: 638651
- Forest area: 211910.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58214
- Scheduled area: 19154.70 ha
- Eligible blocks (age class >= 40): 582140
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.30 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 26.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
