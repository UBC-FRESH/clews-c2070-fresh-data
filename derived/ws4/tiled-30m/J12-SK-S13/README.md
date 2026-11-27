# WS4 tiled 30-m dataset — J12|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J12|SK|S13` (parent `J12|SK`)
- Tile / row / col: `J12` / 1 / 3
- Province: `SK`
- Centroid: 57.446447, -105.041332
- Allocated harvest: 12476.833742 m3
- Productive subcell area: 143243.759432 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1819142
- Blocks: 268402
- Forest area: 163722.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18024
- Scheduled area: 5467.50 ha
- Eligible blocks (age class >= 40): 180238
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.37 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 15.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
