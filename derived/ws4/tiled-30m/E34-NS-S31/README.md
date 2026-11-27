# WS4 tiled 30-m dataset — E34|NS|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E34|NS|S31` (parent `E34|NS`)
- Tile / row / col: `E34` / 3 / 1
- Province: `NS`
- Centroid: 45.649535, -60.549862
- Allocated harvest: 1404.870058 m3
- Productive subcell area: 4930.258840 ha
- Committed geometry area: 6211.961595 ha
- Clipped inventory geometry: 6211.961595 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 56581
- Blocks: 21005
- Forest area: 5092.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1829
- Scheduled area: 416.97 ha
- Eligible blocks (age class >= 40): 18285
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.93 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
