# WS4 tiled 30-m dataset — K14|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K14|MB|S33` (parent `K14|MB`)
- Tile / row / col: `K14` / 3 / 3
- Province: `MB`
- Centroid: 59.919464, -100.282308
- Allocated harvest: 740.915917 m3
- Productive subcell area: 44585.643825 ha
- Committed geometry area: 87995.055250 ha
- Clipped inventory geometry: 87995.055250 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 332942
- Blocks: 156513
- Forest area: 29964.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12454
- Scheduled area: 2289.06 ha
- Eligible blocks (age class >= 40): 124538
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.37 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 5.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
