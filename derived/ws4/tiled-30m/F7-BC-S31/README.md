# WS4 tiled 30-m dataset — F7|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F7|BC|S31` (parent `F7|BC`)
- Tile / row / col: `F7` / 3 / 1
- Province: `BC`
- Centroid: 51.061052, -116.127518
- Allocated harvest: 75971.012035 m3
- Productive subcell area: 114623.758662 ha
- Committed geometry area: 167194.285690 ha
- Clipped inventory geometry: 167194.285690 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1062827
- Blocks: 490807
- Forest area: 95654.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43365
- Scheduled area: 7281.63 ha
- Eligible blocks (age class >= 40): 433644
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.41 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 14.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
