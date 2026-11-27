# WS4 tiled 30-m dataset — H2|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S31` (parent `H2|BC`)
- Tile / row / col: `H2` / 3 / 1
- Province: `BC`
- Centroid: 50.755939, -127.695335
- Allocated harvest: 96446.649652 m3
- Productive subcell area: 109923.277058 ha
- Committed geometry area: 132454.860524 ha
- Clipped inventory geometry: 132454.860524 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1374486
- Blocks: 532496
- Forest area: 123703.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52253
- Scheduled area: 10005.84 ha
- Eligible blocks (age class >= 40): 522521
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.07 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 17.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
