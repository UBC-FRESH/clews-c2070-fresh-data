# WS4 tiled 30-m dataset — E21|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E21|ON|S13` (parent `E21|ON`)
- Tile / row / col: `E21` / 1 / 3
- Province: `ON`
- Centroid: 50.426578, -84.137328
- Allocated harvest: 18244.320301 m3
- Productive subcell area: 126931.838764 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2242014
- Blocks: 820491
- Forest area: 201781.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 80563
- Scheduled area: 19417.41 ha
- Eligible blocks (age class >= 40): 805626
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.69 MB
- Schedules: 0.96 MB
- Runs: 0.00 MB
- Total: 28.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
