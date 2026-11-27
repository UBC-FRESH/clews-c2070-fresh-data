# WS4 tiled 30-m dataset — T4|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T4|YT|S21` (parent `T4|YT`)
- Tile / row / col: `T4` / 2 / 1
- Province: `YT`
- Centroid: 65.595016, -140.770736
- Allocated harvest: 68.419041 m3
- Productive subcell area: 54021.650759 ha
- Committed geometry area: 101316.984307 ha
- Clipped inventory geometry: 101316.984307 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 808950
- Blocks: 299574
- Forest area: 72805.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21928
- Scheduled area: 4191.12 ha
- Eligible blocks (age class >= 40): 219271
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.23 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 10.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
