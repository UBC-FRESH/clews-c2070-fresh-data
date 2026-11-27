# WS4 tiled 30-m dataset — H2|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S33` (parent `H2|BC`)
- Tile / row / col: `H2` / 3 / 3
- Province: `BC`
- Centroid: 51.247050, -126.368984
- Allocated harvest: 179251.013636 m3
- Productive subcell area: 204298.012487 ha
- Committed geometry area: 246174.108647 ha
- Clipped inventory geometry: 246174.108647 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1492448
- Blocks: 875884
- Forest area: 134320.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81309
- Scheduled area: 12026.61 ha
- Eligible blocks (age class >= 40): 813083
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.31 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 23.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
