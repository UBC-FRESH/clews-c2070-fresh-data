# WS4 tiled 30-m dataset — I12|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I12|SK|S12` (parent `I12|SK`)
- Tile / row / col: `I12` / 1 / 2
- Province: `SK`
- Centroid: 56.012169, -105.463902
- Allocated harvest: 23038.876296 m3
- Productive subcell area: 186188.790831 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1879693
- Blocks: 404779
- Forest area: 169172.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25788
- Scheduled area: 5808.06 ha
- Eligible blocks (age class >= 40): 257873
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.08 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 18.38 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
