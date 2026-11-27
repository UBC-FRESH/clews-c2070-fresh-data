# WS4 tiled 30-m dataset — I12|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I12|SK|S33` (parent `I12|SK`)
- Tile / row / col: `I12` / 3 / 3
- Province: `SK`
- Centroid: 56.992203, -104.908930
- Allocated harvest: 23038.876296 m3
- Productive subcell area: 186188.790831 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2200652
- Blocks: 296221
- Forest area: 198058.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21068
- Scheduled area: 9903.06 ha
- Eligible blocks (age class >= 40): 210677
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.49 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 18.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
