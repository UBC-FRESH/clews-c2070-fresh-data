# WS4 tiled 30-m dataset — J2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S33` (parent `J2|BC`)
- Tile / row / col: `J2` / 3 / 3
- Province: `BC`
- Centroid: 53.627763, -128.531340
- Allocated harvest: 122308.070918 m3
- Productive subcell area: 161226.193119 ha
- Committed geometry area: 220812.741413 ha
- Clipped inventory geometry: 220812.741413 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1701183
- Blocks: 924225
- Forest area: 153106.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87774
- Scheduled area: 13622.22 ha
- Eligible blocks (age class >= 40): 877733
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.41 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 25.46 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
