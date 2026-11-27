# WS4 tiled 30-m dataset — K15|MB|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K15|MB|S11` (parent `K15|MB`)
- Tile / row / col: `K15` / 1 / 1
- Province: `MB`
- Centroid: 59.183012, -99.243866
- Allocated harvest: 1788.924924 m3
- Productive subcell area: 104044.388366 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1259687
- Blocks: 407554
- Forest area: 113371.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28260
- Scheduled area: 7520.58 ha
- Eligible blocks (age class >= 40): 282599
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.66 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 15.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
