# WS4 tiled 30-m dataset — F15|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F15|MB|S23` (parent `F15|MB`)
- Tile / row / col: `F15` / 2 / 3
- Province: `MB`
- Centroid: 52.814551, -97.042717
- Allocated harvest: 3928.297390 m3
- Productive subcell area: 94387.498312 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2163859
- Blocks: 730075
- Forest area: 194747.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67961
- Scheduled area: 16535.70 ha
- Eligible blocks (age class >= 40): 679604
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.84 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 26.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
