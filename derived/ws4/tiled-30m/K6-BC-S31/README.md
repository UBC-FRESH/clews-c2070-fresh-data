# WS4 tiled 30-m dataset — K6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K6|BC|S31` (parent `K6|BC`)
- Tile / row / col: `K6` / 3 / 1
- Province: `BC`
- Centroid: 56.963602, -122.543371
- Allocated harvest: 98740.202921 m3
- Productive subcell area: 214208.343932 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2671735
- Blocks: 1343313
- Forest area: 240456.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 126841
- Scheduled area: 21246.66 ha
- Eligible blocks (age class >= 40): 1268402
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 37.99 MB
- Schedules: 1.54 MB
- Runs: 0.00 MB
- Total: 39.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
