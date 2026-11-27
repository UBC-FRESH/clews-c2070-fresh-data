# WS4 tiled 30-m dataset — J10|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J10|SK|S33` (parent `J10|SK`)
- Tile / row / col: `J10` / 3 / 3
- Province: `SK`
- Centroid: 57.694635, -109.969440
- Allocated harvest: 687.181324 m3
- Productive subcell area: 5165.660971 ha
- Committed geometry area: 6273.247425 ha
- Clipped inventory geometry: 6273.247425 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 54134
- Blocks: 7832
- Forest area: 4872.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4633
- Scheduled area: 2411.46 ha
- Eligible blocks (age class >= 40): 4633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.61 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 0.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
