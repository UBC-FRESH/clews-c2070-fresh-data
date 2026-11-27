# WS4 tiled 30-m dataset — S7|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S7|NT|S23` (parent `S7|NT`)
- Tile / row / col: `S7` / 2 / 3
- Province: `NT`
- Centroid: 67.461005, -128.705250
- Allocated harvest: 144.012293 m3
- Productive subcell area: 207402.854424 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1818010
- Blocks: 840041
- Forest area: 163620.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63204
- Scheduled area: 10814.67 ha
- Eligible blocks (age class >= 40): 632038
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.49 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 25.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
