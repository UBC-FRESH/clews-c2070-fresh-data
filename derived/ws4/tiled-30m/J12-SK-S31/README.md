# WS4 tiled 30-m dataset — J12|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J12|SK|S31` (parent `J12|SK`)
- Tile / row / col: `J12` / 3 / 1
- Province: `SK`
- Centroid: 58.194407, -107.038977
- Allocated harvest: 12476.833742 m3
- Productive subcell area: 143243.759432 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1584745
- Blocks: 255938
- Forest area: 142627.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9810
- Scheduled area: 1813.59 ha
- Eligible blocks (age class >= 40): 98091
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.02 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 14.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
