# WS4 tiled 30-m dataset — G6|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G6|BC|S33` (parent `G6|BC`)
- Tile / row / col: `G6` / 3 / 3
- Province: `BC`
- Centroid: 52.137974, -117.622679
- Allocated harvest: 32640.137824 m3
- Productive subcell area: 45577.947836 ha
- Committed geometry area: 78157.970726 ha
- Clipped inventory geometry: 78157.970726 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 213479
- Blocks: 115246
- Forest area: 19213.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10211
- Scheduled area: 1440.90 ha
- Eligible blocks (age class >= 40): 102106
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.89 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
