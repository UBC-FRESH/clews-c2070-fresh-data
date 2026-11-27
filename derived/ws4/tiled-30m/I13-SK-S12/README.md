# WS4 tiled 30-m dataset — I13|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S12` (parent `I13|SK`)
- Tile / row / col: `I13` / 1 / 2
- Province: `SK`
- Centroid: 56.211605, -103.025709
- Allocated harvest: 27419.892255 m3
- Productive subcell area: 171206.562836 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2043477
- Blocks: 310913
- Forest area: 183912.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20886
- Scheduled area: 9036.63 ha
- Eligible blocks (age class >= 40): 208856
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.75 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 17.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
