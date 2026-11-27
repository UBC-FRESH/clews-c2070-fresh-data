# WS4 tiled 30-m dataset — T5|YT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|YT|S32` (parent `T5|YT`)
- Tile / row / col: `T5` / 3 / 2
- Province: `YT`
- Centroid: 67.139155, -138.316237
- Allocated harvest: 216.789563 m3
- Productive subcell area: 131519.529150 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1272786
- Blocks: 406303
- Forest area: 114550.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24730
- Scheduled area: 5108.85 ha
- Eligible blocks (age class >= 40): 247294
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.66 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 14.95 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
