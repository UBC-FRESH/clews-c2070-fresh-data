# WS4 tiled 30-m dataset — L10|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|NT|S23` (parent `L10|NT`)
- Tile / row / col: `L10` / 2 / 3
- Province: `NT`
- Centroid: 60.130504, -111.551196
- Allocated harvest: 141.281181 m3
- Productive subcell area: 88449.601487 ha
- Committed geometry area: 143034.764273 ha
- Clipped inventory geometry: 143034.764273 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1162384
- Blocks: 548035
- Forest area: 104614.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46146
- Scheduled area: 7555.77 ha
- Eligible blocks (age class >= 40): 461454
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.04 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 16.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
