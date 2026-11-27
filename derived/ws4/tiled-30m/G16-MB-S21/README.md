# WS4 tiled 30-m dataset — G16|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G16|MB|S21` (parent `G16|MB`)
- Tile / row / col: `G16` / 2 / 1
- Province: `MB`
- Centroid: 54.194498, -96.338952
- Allocated harvest: 7060.965475 m3
- Productive subcell area: 187107.934041 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1991091
- Blocks: 581812
- Forest area: 179198.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46752
- Scheduled area: 9693.72 ha
- Eligible blocks (age class >= 40): 467514
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.71 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 22.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
