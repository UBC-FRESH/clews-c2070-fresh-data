# WS4 tiled 30-m dataset — E18|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E18|ON|S21` (parent `E18|ON`)
- Tile / row / col: `E18` / 2 / 1
- Province: `ON`
- Centroid: 51.423941, -91.893849
- Allocated harvest: 44053.319318 m3
- Productive subcell area: 196383.006621 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2140705
- Blocks: 617124
- Forest area: 192663.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56102
- Scheduled area: 13674.78 ha
- Eligible blocks (age class >= 40): 561011
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.71 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 24.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
