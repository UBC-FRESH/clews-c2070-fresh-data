# WS4 tiled 30-m dataset — Q7|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q7|NT|S33` (parent `Q7|NT`)
- Tile / row / col: `Q7` / 3 / 3
- Province: `NT`
- Centroid: 65.441446, -125.895516
- Allocated harvest: 140.807692 m3
- Productive subcell area: 144411.735102 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1936270
- Blocks: 484300
- Forest area: 174264.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38565
- Scheduled area: 13283.28 ha
- Eligible blocks (age class >= 40): 385642
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.88 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 20.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
