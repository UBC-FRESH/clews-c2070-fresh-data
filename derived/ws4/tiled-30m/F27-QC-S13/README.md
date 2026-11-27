# WS4 tiled 30-m dataset — F27|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F27|QC|S13` (parent `F27|QC`)
- Tile / row / col: `F27` / 1 / 3
- Province: `QC`
- Centroid: 49.554118, -71.416265
- Allocated harvest: 69235.179569 m3
- Productive subcell area: 200501.689283 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2133836
- Blocks: 669737
- Forest area: 192045.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48966
- Scheduled area: 11098.89 ha
- Eligible blocks (age class >= 40): 489655
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.56 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 25.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
