# WS4 tiled 30-m dataset — G19|ON|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G19|ON|S32` (parent `G19|ON`)
- Tile / row / col: `G19` / 3 / 2
- Province: `ON`
- Centroid: 54.465896, -88.488061
- Allocated harvest: 14178.961437 m3
- Productive subcell area: 168654.852009 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1414296
- Blocks: 631570
- Forest area: 127286.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57623
- Scheduled area: 11977.47 ha
- Eligible blocks (age class >= 40): 576224
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.17 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 19.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
