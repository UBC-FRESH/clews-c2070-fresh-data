# WS4 tiled 30-m dataset — H17|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H17|MB|S31` (parent `H17|MB`)
- Tile / row / col: `H17` / 3 / 1
- Province: `MB`
- Centroid: 56.029569, -93.949598
- Allocated harvest: 3671.317445 m3
- Productive subcell area: 166044.572865 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2034555
- Blocks: 837383
- Forest area: 183109.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69812
- Scheduled area: 13901.31 ha
- Eligible blocks (age class >= 40): 698115
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.76 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 26.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
