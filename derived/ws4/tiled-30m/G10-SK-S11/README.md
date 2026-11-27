# WS4 tiled 30-m dataset — G10|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|SK|S11` (parent `G10|SK`)
- Tile / row / col: `G10` / 1 / 1
- Province: `SK`
- Centroid: 52.693210, -109.769576
- Allocated harvest: 13481.001879 m3
- Productive subcell area: 56064.892292 ha
- Committed geometry area: 160129.438442 ha
- Clipped inventory geometry: 160129.438442 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 368333
- Blocks: 124817
- Forest area: 33149.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5400
- Scheduled area: 1895.04 ha
- Eligible blocks (age class >= 40): 53999
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.01 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 5.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
