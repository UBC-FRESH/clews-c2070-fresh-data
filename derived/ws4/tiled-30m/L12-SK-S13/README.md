# WS4 tiled 30-m dataset — L12|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L12|SK|S13` (parent `L12|SK`)
- Tile / row / col: `L12` / 1 / 3
- Province: `SK`
- Centroid: 59.969125, -105.960194
- Allocated harvest: 1377.017525 m3
- Productive subcell area: 18226.612056 ha
- Committed geometry area: 29050.713377 ha
- Clipped inventory geometry: 29050.713377 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 129580
- Blocks: 49772
- Forest area: 11662.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3726
- Scheduled area: 787.59 ha
- Eligible blocks (age class >= 40): 37259
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.08 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
