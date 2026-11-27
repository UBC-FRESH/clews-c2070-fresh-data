# WS4 tiled 30-m dataset — G19|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G19|ON|S11` (parent `G19|ON`)
- Tile / row / col: `G19` / 1 / 1
- Province: `ON`
- Centroid: 53.599938, -89.407826
- Allocated harvest: 14178.961437 m3
- Productive subcell area: 168654.852009 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2156837
- Blocks: 573081
- Forest area: 194115.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55568
- Scheduled area: 28896.03 ha
- Eligible blocks (age class >= 40): 555673
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.26 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 23.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
