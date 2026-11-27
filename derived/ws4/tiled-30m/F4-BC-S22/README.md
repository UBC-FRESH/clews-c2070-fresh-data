# WS4 tiled 30-m dataset — F4|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S22` (parent `F4|BC`)
- Tile / row / col: `F4` / 2 / 2
- Province: `BC`
- Centroid: 49.382059, -121.042991
- Allocated harvest: 187932.035561 m3
- Productive subcell area: 186912.489401 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2513720
- Blocks: 1338373
- Forest area: 226234.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 126786
- Scheduled area: 19315.89 ha
- Eligible blocks (age class >= 40): 1267854
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 36.73 MB
- Schedules: 1.54 MB
- Runs: 0.00 MB
- Total: 38.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
