# WS4 tiled 30-m dataset — J33|NL|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|NL|S23` (parent `J33|NL`)
- Tile / row / col: `J33` / 2 / 3
- Province: `NL`
- Centroid: 50.956580, -56.022610
- Allocated harvest: 3612.656989 m3
- Productive subcell area: 76319.670257 ha
- Committed geometry area: 115012.442310 ha
- Clipped inventory geometry: 115012.442310 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1045766
- Blocks: 526290
- Forest area: 94118.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49785
- Scheduled area: 8265.15 ha
- Eligible blocks (age class >= 40): 497849
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.86 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 15.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
