# WS4 tiled 30-m dataset — Q6|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q6|YT|S31` (parent `Q6|YT`)
- Tile / row / col: `Q6` / 3 / 1
- Province: `YT`
- Centroid: 64.241838, -131.072348
- Allocated harvest: 8.355501 m3
- Productive subcell area: 7478.412001 ha
- Committed geometry area: 29623.996921 ha
- Clipped inventory geometry: 29623.996921 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 9169
- Blocks: 5747
- Forest area: 825.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 583
- Scheduled area: 74.34 ha
- Eligible blocks (age class >= 40): 583
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.24 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
