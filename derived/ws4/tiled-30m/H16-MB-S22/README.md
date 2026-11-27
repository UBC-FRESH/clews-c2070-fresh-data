# WS4 tiled 30-m dataset — H16|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H16|MB|S22` (parent `H16|MB`)
- Tile / row / col: `H16` / 2 / 2
- Province: `MB`
- Centroid: 55.574298, -95.581109
- Allocated harvest: 5853.763982 m3
- Productive subcell area: 184419.845316 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2073749
- Blocks: 590022
- Forest area: 186637.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52377
- Scheduled area: 14367.60 ha
- Eligible blocks (age class >= 40): 523766
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.77 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 23.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
