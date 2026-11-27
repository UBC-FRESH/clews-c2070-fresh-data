# WS4 tiled 30-m dataset — J6|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S12` (parent `J6|BC`)
- Tile / row / col: `J6` / 1 / 2
- Province: `BC`
- Centroid: 55.043907, -120.264611
- Allocated harvest: 82387.266717 m3
- Productive subcell area: 146387.228871 ha
- Committed geometry area: 174498.994275 ha
- Clipped inventory geometry: 174498.994275 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1696358
- Blocks: 804145
- Forest area: 152672.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75099
- Scheduled area: 12669.75 ha
- Eligible blocks (age class >= 40): 750981
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.18 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 24.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
