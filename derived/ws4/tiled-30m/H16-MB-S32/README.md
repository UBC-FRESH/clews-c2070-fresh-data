# WS4 tiled 30-m dataset — H16|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H16|MB|S32` (parent `H16|MB`)
- Tile / row / col: `H16` / 3 / 2
- Province: `MB`
- Centroid: 56.032901, -95.588596
- Allocated harvest: 5853.763982 m3
- Productive subcell area: 184419.845316 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1785548
- Blocks: 472978
- Forest area: 160699.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35108
- Scheduled area: 10774.08 ha
- Eligible blocks (age class >= 40): 351079
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.06 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 19.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
