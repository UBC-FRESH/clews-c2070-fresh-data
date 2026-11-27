# WS4 tiled 30-m dataset — J6|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S33` (parent `J6|BC`)
- Tile / row / col: `J6` / 3 / 3
- Province: `BC`
- Centroid: 56.058522, -120.210278
- Allocated harvest: 62147.541454 m3
- Productive subcell area: 110424.908327 ha
- Committed geometry area: 131630.577302 ha
- Clipped inventory geometry: 131630.577302 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 558949
- Blocks: 216084
- Forest area: 50305.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17818
- Scheduled area: 4213.35 ha
- Eligible blocks (age class >= 40): 178174
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.62 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 7.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
