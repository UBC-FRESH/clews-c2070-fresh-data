# WS4 tiled 30-m dataset — G3|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G3|BC|S22` (parent `G3|BC`)
- Tile / row / col: `G3` / 2 / 2
- Province: `BC`
- Centroid: 50.098653, -123.639000
- Allocated harvest: 140768.168260 m3
- Productive subcell area: 161344.689531 ha
- Committed geometry area: 227063.625036 ha
- Clipped inventory geometry: 227063.625036 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1712802
- Blocks: 950041
- Forest area: 154152.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88325
- Scheduled area: 13538.16 ha
- Eligible blocks (age class >= 40): 883246
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.91 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 25.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
