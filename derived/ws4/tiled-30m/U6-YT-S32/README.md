# WS4 tiled 30-m dataset — U6|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U6|YT|S32` (parent `U6|YT`)
- Tile / row / col: `U6` / 3 / 2
- Province: `YT`
- Centroid: 68.986991, -137.967148
- Allocated harvest: 17.825637 m3
- Productive subcell area: 9614.993670 ha
- Committed geometry area: 111942.188238 ha
- Clipped inventory geometry: 111942.188238 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 14500
- Blocks: 10295
- Forest area: 1305.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4352
- Scheduled area: 512.37 ha
- Eligible blocks (age class >= 40): 4352
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.37 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
