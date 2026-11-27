# WS4 tiled 30-m dataset — U5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U5|YT|S23` (parent `U5|YT`)
- Tile / row / col: `U5` / 2 / 3
- Province: `YT`
- Centroid: 68.145964, -138.913252
- Allocated harvest: 141.204389 m3
- Productive subcell area: 81768.351812 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 231747
- Blocks: 100089
- Forest area: 20857.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5410
- Scheduled area: 1159.92 ha
- Eligible blocks (age class >= 40): 54100
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.69 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
