# WS4 tiled 30-m dataset — H17|ON|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H17|ON|S13` (parent `H17|ON`)
- Tile / row / col: `H17` / 1 / 3
- Province: `ON`
- Centroid: 54.869268, -92.024927
- Allocated harvest: 132.388111 m3
- Productive subcell area: 1373.420551 ha
- Committed geometry area: 1732.951715 ha
- Clipped inventory geometry: 1732.951715 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 17616
- Blocks: 6965
- Forest area: 1585.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 692
- Scheduled area: 150.12 ha
- Eligible blocks (age class >= 40): 6920
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.34 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
