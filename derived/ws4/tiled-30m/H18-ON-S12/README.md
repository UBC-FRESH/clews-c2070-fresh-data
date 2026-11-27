# WS4 tiled 30-m dataset — H18|ON|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|ON|S12` (parent `H18|ON`)
- Tile / row / col: `H18` / 1 / 2
- Province: `ON`
- Centroid: 55.037497, -90.786204
- Allocated harvest: 10535.772862 m3
- Productive subcell area: 131722.308145 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1880757
- Blocks: 701350
- Forest area: 169268.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62360
- Scheduled area: 14379.66 ha
- Eligible blocks (age class >= 40): 623596
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.06 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 23.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
