# WS4 tiled 30-m dataset — C24|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C24|QC|S13` (parent `C24|QC`)
- Tile / row / col: `C24` / 1 / 3
- Province: `QC`
- Centroid: 46.957681, -78.986962
- Allocated harvest: 97276.110333 m3
- Productive subcell area: 174544.100365 ha
- Committed geometry area: 221992.604606 ha
- Clipped inventory geometry: 221992.604606 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1868557
- Blocks: 676344
- Forest area: 168170.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62952
- Scheduled area: 14991.57 ha
- Eligible blocks (age class >= 40): 629513
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.11 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 23.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
