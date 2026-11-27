# WS4 tiled 30-m dataset — C18|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C18|ON|S33` (parent `C18|ON`)
- Tile / row / col: `C18` / 3 / 3
- Province: `ON`
- Centroid: 49.116993, -90.692183
- Allocated harvest: 42978.519913 m3
- Productive subcell area: 198681.129932 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2386584
- Blocks: 784001
- Forest area: 214792.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68567
- Scheduled area: 15855.75 ha
- Eligible blocks (age class >= 40): 685667
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.16 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 28.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
