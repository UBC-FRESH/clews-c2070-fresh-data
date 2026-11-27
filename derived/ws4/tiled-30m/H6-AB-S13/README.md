# WS4 tiled 30-m dataset — H6|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|AB|S13` (parent `H6|AB`)
- Tile / row / col: `H6` / 1 / 3
- Province: `AB`
- Centroid: 52.674567, -117.719476
- Allocated harvest: 112513.596841 m3
- Productive subcell area: 140278.571989 ha
- Committed geometry area: 243267.458015 ha
- Clipped inventory geometry: 243267.458015 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1190604
- Blocks: 582046
- Forest area: 107154.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53381
- Scheduled area: 8973.00 ha
- Eligible blocks (age class >= 40): 533807
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.05 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 17.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
