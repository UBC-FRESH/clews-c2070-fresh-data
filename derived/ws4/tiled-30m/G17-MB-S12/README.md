# WS4 tiled 30-m dataset — G17|MB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G17|MB|S12` (parent `G17|MB`)
- Tile / row / col: `G17` / 1 / 2
- Province: `MB`
- Centroid: 53.892944, -93.529568
- Allocated harvest: 560.697326 m3
- Productive subcell area: 15657.554568 ha
- Committed geometry area: 21169.586540 ha
- Clipped inventory geometry: 21169.586540 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 193192
- Blocks: 46069
- Forest area: 17387.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3156
- Scheduled area: 566.37 ha
- Eligible blocks (age class >= 40): 31556
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.31 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
