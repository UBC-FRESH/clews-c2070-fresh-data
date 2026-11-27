# WS4 tiled 30-m dataset — G5|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G5|BC|S11` (parent `G5|BC`)
- Tile / row / col: `G5` / 1 / 1
- Province: `BC`
- Centroid: 50.566319, -120.305836
- Allocated harvest: 139454.892072 m3
- Productive subcell area: 210408.981546 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1698824
- Blocks: 632727
- Forest area: 152894.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52484
- Scheduled area: 9471.51 ha
- Eligible blocks (age class >= 40): 524834
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.92 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 21.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
