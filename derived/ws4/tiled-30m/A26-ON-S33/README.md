# WS4 tiled 30-m dataset — A26|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A26|ON|S33` (parent `A26|ON`)
- Tile / row / col: `A26` / 3 / 3
- Province: `ON`
- Centroid: 44.544478, -76.080777
- Allocated harvest: 28080.337191 m3
- Productive subcell area: 111822.161073 ha
- Committed geometry area: 206353.786467 ha
- Clipped inventory geometry: 206353.786467 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1239045
- Blocks: 483683
- Forest area: 111514.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40008
- Scheduled area: 9462.15 ha
- Eligible blocks (age class >= 40): 400077
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.99 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 16.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
