# WS4 tiled 30-m dataset — E13|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|SK|S21` (parent `E13|SK`)
- Tile / row / col: `E13` / 2 / 1
- Province: `SK`
- Centroid: 51.175320, -102.743052
- Allocated harvest: 7564.483900 m3
- Productive subcell area: 34376.961027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 190005
- Blocks: 83577
- Forest area: 17100.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4776
- Scheduled area: 1212.66 ha
- Eligible blocks (age class >= 40): 47755
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.08 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 3.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
