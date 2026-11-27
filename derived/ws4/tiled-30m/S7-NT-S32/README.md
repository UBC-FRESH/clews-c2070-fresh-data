# WS4 tiled 30-m dataset — S7|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S7|NT|S32` (parent `S7|NT`)
- Tile / row / col: `S7` / 3 / 2
- Province: `NT`
- Centroid: 67.617770, -130.362557
- Allocated harvest: 144.012293 m3
- Productive subcell area: 207402.854424 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1826233
- Blocks: 649185
- Forest area: 164360.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44089
- Scheduled area: 9694.17 ha
- Eligible blocks (age class >= 40): 440882
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.90 MB
- Schedules: 0.52 MB
- Runs: 0.00 MB
- Total: 22.42 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
