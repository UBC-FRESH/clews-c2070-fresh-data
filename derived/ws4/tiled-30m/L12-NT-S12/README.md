# WS4 tiled 30-m dataset — L12|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|NT|S12` (parent `L12|NT`)
- Tile / row / col: `L12` / 1 / 2
- Province: `NT`
- Centroid: 60.161105, -106.831513
- Allocated harvest: 42.536850 m3
- Productive subcell area: 95003.967848 ha
- Committed geometry area: 175966.583015 ha
- Clipped inventory geometry: 175966.583015 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1137380
- Blocks: 358957
- Forest area: 102364.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27779
- Scheduled area: 11513.79 ha
- Eligible blocks (age class >= 40): 277785
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.07 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 13.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
