# WS4 tiled 30-m dataset — H6|AB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S31` (parent `H6|AB`)
- Tile / row / col: `H6` / 3 / 1
- Province: `AB`
- Centroid: 53.410178, -119.549103
- Allocated harvest: 8448.252434 m3
- Productive subcell area: 10533.027300 ha
- Committed geometry area: 18266.102515 ha
- Clipped inventory geometry: 18266.102515 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 55749
- Blocks: 33606
- Forest area: 5017.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3165
- Scheduled area: 467.10 ha
- Eligible blocks (age class >= 40): 31650
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.16 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
