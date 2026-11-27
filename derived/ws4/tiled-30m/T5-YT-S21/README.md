# WS4 tiled 30-m dataset — T5|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|YT|S21` (parent `T5|YT`)
- Tile / row / col: `T5` / 2 / 1
- Province: `YT`
- Centroid: 66.489246, -138.486772
- Allocated harvest: 216.789563 m3
- Productive subcell area: 131519.529150 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2036512
- Blocks: 621001
- Forest area: 183286.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48838
- Scheduled area: 12529.53 ha
- Eligible blocks (age class >= 40): 488371
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.96 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 23.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
