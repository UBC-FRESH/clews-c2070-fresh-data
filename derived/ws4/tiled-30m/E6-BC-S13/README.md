# WS4 tiled 30-m dataset — E6|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E6|BC|S13` (parent `E6|BC`)
- Tile / row / col: `E6` / 1 / 3
- Province: `BC`
- Centroid: 49.038789, -115.519593
- Allocated harvest: 20407.160264 m3
- Productive subcell area: 22147.649157 ha
- Committed geometry area: 26646.533891 ha
- Clipped inventory geometry: 26646.533891 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 278157
- Blocks: 87710
- Forest area: 25034.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7725
- Scheduled area: 1583.01 ha
- Eligible blocks (age class >= 40): 77247
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.76 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
