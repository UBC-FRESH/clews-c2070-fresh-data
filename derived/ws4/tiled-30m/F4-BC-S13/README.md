# WS4 tiled 30-m dataset — F4|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S13` (parent `F4|BC`)
- Tile / row / col: `F4` / 1 / 3
- Province: `BC`
- Centroid: 49.180469, -120.134896
- Allocated harvest: 158292.529544 m3
- Productive subcell area: 157433.780049 ha
- Committed geometry area: 210571.509364 ha
- Clipped inventory geometry: 210571.509364 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1825504
- Blocks: 625942
- Forest area: 164295.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54419
- Scheduled area: 9490.23 ha
- Eligible blocks (age class >= 40): 544189
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.50 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 22.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
