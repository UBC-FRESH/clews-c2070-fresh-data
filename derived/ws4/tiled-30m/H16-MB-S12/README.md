# WS4 tiled 30-m dataset — H16|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H16|MB|S12` (parent `H16|MB`)
- Tile / row / col: `H16` / 1 / 2
- Province: `MB`
- Centroid: 55.116152, -95.573810
- Allocated harvest: 5853.763982 m3
- Productive subcell area: 184419.845316 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2040636
- Blocks: 820745
- Forest area: 183657.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 79101
- Scheduled area: 16747.65 ha
- Eligible blocks (age class >= 40): 791004
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.93 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 26.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
