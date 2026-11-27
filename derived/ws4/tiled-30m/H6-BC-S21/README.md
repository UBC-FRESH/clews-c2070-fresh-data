# WS4 tiled 30-m dataset — H6|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S21` (parent `H6|BC`)
- Tile / row / col: `H6` / 2 / 1
- Province: `BC`
- Centroid: 52.762615, -119.393429
- Allocated harvest: 87704.520276 m3
- Productive subcell area: 148704.411178 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1622701
- Blocks: 851373
- Forest area: 146043.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77968
- Scheduled area: 11852.19 ha
- Eligible blocks (age class >= 40): 779674
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.33 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 24.25 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
