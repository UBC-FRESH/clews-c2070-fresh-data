# WS4 tiled 30-m dataset — U7|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S12` (parent `U7|NT`)
- Tile / row / col: `U7` / 1 / 2
- Province: `NT`
- Centroid: 69.180985, -133.159513
- Allocated harvest: 11.339258 m3
- Productive subcell area: 9694.068509 ha
- Committed geometry area: 193485.416028 ha
- Clipped inventory geometry: 193485.416028 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 173592
- Blocks: 120125
- Forest area: 15623.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5516
- Scheduled area: 590.85 ha
- Eligible blocks (age class >= 40): 55157
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.64 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
