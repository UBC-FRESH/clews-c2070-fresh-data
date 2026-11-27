# WS4 tiled 30-m dataset — B26|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|ON|S23` (parent `B26|ON`)
- Tile / row / col: `B26` / 2 / 3
- Province: `ON`
- Centroid: 45.304853, -75.654446
- Allocated harvest: 44714.261845 m3
- Productive subcell area: 147977.569645 ha
- Committed geometry area: 186141.219844 ha
- Clipped inventory geometry: 186141.219844 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 775678
- Blocks: 298100
- Forest area: 69811.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21332
- Scheduled area: 4843.53 ha
- Eligible blocks (age class >= 40): 213315
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.11 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 10.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
