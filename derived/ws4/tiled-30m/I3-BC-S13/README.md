# WS4 tiled 30-m dataset — I3|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I3|BC|S13` (parent `I3|BC`)
- Tile / row / col: `I3` / 1 / 3
- Province: `BC`
- Centroid: 52.275752, -124.764518
- Allocated harvest: 88119.082702 m3
- Productive subcell area: 179352.040200 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2602635
- Blocks: 679838
- Forest area: 234237.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63888
- Scheduled area: 18278.01 ha
- Eligible blocks (age class >= 40): 638877
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.04 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 28.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
