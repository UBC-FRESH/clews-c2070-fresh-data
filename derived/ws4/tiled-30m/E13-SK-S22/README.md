# WS4 tiled 30-m dataset — E13|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|SK|S22` (parent `E13|SK`)
- Tile / row / col: `E13` / 2 / 2
- Province: `SK`
- Centroid: 51.227801, -102.026793
- Allocated harvest: 7564.483900 m3
- Productive subcell area: 34376.961027 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 192134
- Blocks: 78313
- Forest area: 17292.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5002
- Scheduled area: 1197.54 ha
- Eligible blocks (age class >= 40): 50015
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.99 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 3.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
