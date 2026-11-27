# WS4 tiled 30-m dataset — F29|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S33` (parent `F29|QC`)
- Tile / row / col: `F29` / 3 / 3
- Province: `QC`
- Centroid: 49.436396, -67.305969
- Allocated harvest: 6136.919697 m3
- Productive subcell area: 13324.947554 ha
- Committed geometry area: 15872.167755 ha
- Clipped inventory geometry: 15872.167755 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 159641
- Blocks: 77953
- Forest area: 14367.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7362
- Scheduled area: 1276.20 ha
- Eligible blocks (age class >= 40): 73619
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.86 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 2.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
