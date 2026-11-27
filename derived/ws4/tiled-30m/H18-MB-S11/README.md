# WS4 tiled 30-m dataset — H18|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|MB|S11` (parent `H18|MB`)
- Tile / row / col: `H18` / 1 / 1
- Province: `MB`
- Centroid: 55.168761, -91.804795
- Allocated harvest: 842.184706 m3
- Productive subcell area: 41765.020724 ha
- Committed geometry area: 68088.221492 ha
- Clipped inventory geometry: 68088.221492 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 578332
- Blocks: 244159
- Forest area: 52049.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23029
- Scheduled area: 5735.70 ha
- Eligible blocks (age class >= 40): 230284
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.08 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 8.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
