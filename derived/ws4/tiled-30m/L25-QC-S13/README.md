# WS4 tiled 30-m dataset — L25|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L25|QC|S13` (parent `L25|QC`)
- Tile / row / col: `L25` / 1 / 3
- Province: `QC`
- Centroid: 58.196864, -70.605019
- Allocated harvest: 908.419413 m3
- Productive subcell area: 6964.015037 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 69613
- Blocks: 40644
- Forest area: 6265.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2141
- Scheduled area: 327.78 ha
- Eligible blocks (age class >= 40): 21406
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.38 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
