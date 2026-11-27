# WS4 tiled 30-m dataset — J12|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J12|SK|S21` (parent `J12|SK`)
- Tile / row / col: `J12` / 2 / 1
- Province: `SK`
- Centroid: 57.742055, -106.877028
- Allocated harvest: 12476.833742 m3
- Productive subcell area: 143243.759432 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1253053
- Blocks: 247544
- Forest area: 112774.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11597
- Scheduled area: 2196.36 ha
- Eligible blocks (age class >= 40): 115961
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.01 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 12.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
