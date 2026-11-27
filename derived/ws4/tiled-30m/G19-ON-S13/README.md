# WS4 tiled 30-m dataset — G19|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G19|ON|S13` (parent `G19|ON`)
- Tile / row / col: `G19` / 1 / 3
- Province: `ON`
- Centroid: 53.508939, -87.883316
- Allocated harvest: 14178.961437 m3
- Productive subcell area: 168654.852009 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2028903
- Blocks: 581199
- Forest area: 182601.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53859
- Scheduled area: 15391.08 ha
- Eligible blocks (age class >= 40): 538590
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.26 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 22.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
