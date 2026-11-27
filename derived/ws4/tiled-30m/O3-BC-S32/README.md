# WS4 tiled 30-m dataset — O3|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|BC|S32` (parent `O3|BC`)
- Tile / row / col: `O3` / 3 / 2
- Province: `BC`
- Centroid: 59.858383, -133.911199
- Allocated harvest: 39035.091676 m3
- Productive subcell area: 95896.968630 ha
- Committed geometry area: 172984.323200 ha
- Clipped inventory geometry: 172984.323200 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1387400
- Blocks: 749914
- Forest area: 124866.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 71941
- Scheduled area: 12413.25 ha
- Eligible blocks (age class >= 40): 719408
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.54 MB
- Schedules: 0.85 MB
- Runs: 0.00 MB
- Total: 21.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
