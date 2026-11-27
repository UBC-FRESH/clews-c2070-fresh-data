# WS4 tiled 30-m dataset — G33|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G33|NL|S33` (parent `G33|NL`)
- Tile / row / col: `G33` / 3 / 3
- Province: `NL`
- Centroid: 47.886259, -58.950099
- Allocated harvest: 8517.771199 m3
- Productive subcell area: 144127.639593 ha
- Committed geometry area: 233970.535676 ha
- Clipped inventory geometry: 233970.535676 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1627941
- Blocks: 687017
- Forest area: 146514.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 56070
- Scheduled area: 12039.30 ha
- Eligible blocks (age class >= 40): 560696
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.45 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 22.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
