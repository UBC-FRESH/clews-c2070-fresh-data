# WS4 tiled 30-m dataset — K1|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K1|BC|S12` (parent `K1|BC`)
- Tile / row / col: `K1` / 1 / 2
- Province: `BC`
- Centroid: 53.034171, -131.803959
- Allocated harvest: 54806.402647 m3
- Productive subcell area: 58377.063929 ha
- Committed geometry area: 62347.153241 ha
- Clipped inventory geometry: 62347.153241 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 669477
- Blocks: 279336
- Forest area: 60252.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27610
- Scheduled area: 5363.55 ha
- Eligible blocks (age class >= 40): 276092
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.87 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 9.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
