# WS4 tiled 30-m dataset — G3|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S13` (parent `G3|BC`)
- Tile / row / col: `G3` / 1 / 3
- Province: `BC`
- Centroid: 49.832918, -122.877402
- Allocated harvest: 154968.364534 m3
- Productive subcell area: 177620.572690 ha
- Committed geometry area: 249969.002594 ha
- Clipped inventory geometry: 249969.002594 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1743443
- Blocks: 963386
- Forest area: 156909.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 90226
- Scheduled area: 13498.56 ha
- Eligible blocks (age class >= 40): 902252
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.26 MB
- Schedules: 1.07 MB
- Runs: 0.00 MB
- Total: 26.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
