# WS4 tiled 30-m dataset — E7|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|BC|S22` (parent `E7|BC`)
- Tile / row / col: `E7` / 2 / 2
- Province: `BC`
- Centroid: 49.490130, -114.711051
- Allocated harvest: 49914.768274 m3
- Productive subcell area: 58794.012446 ha
- Committed geometry area: 78506.042754 ha
- Clipped inventory geometry: 78506.042754 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 699248
- Blocks: 350327
- Forest area: 62932.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31173
- Scheduled area: 4805.10 ha
- Eligible blocks (age class >= 40): 311722
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.30 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 10.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
