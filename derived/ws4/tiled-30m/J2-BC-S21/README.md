# WS4 tiled 30-m dataset — J2|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J2|BC|S21` (parent `J2|BC`)
- Tile / row / col: `J2` / 2 / 1
- Province: `BC`
- Centroid: 52.794311, -129.227737
- Allocated harvest: 20492.318995 m3
- Productive subcell area: 27012.923636 ha
- Committed geometry area: 36996.455763 ha
- Clipped inventory geometry: 36996.455763 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 384425
- Blocks: 180100
- Forest area: 34598.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17835
- Scheduled area: 3494.34 ha
- Eligible blocks (age class >= 40): 178347
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.02 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 6.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
