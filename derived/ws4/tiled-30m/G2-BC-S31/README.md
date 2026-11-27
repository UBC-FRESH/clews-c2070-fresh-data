# WS4 tiled 30-m dataset — G2|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S31` (parent `G2|BC`)
- Tile / row / col: `G2` / 3 / 1
- Province: `BC`
- Centroid: 49.669337, -126.523595
- Allocated harvest: 136388.061217 m3
- Productive subcell area: 134196.508473 ha
- Committed geometry area: 147688.155311 ha
- Clipped inventory geometry: 147688.155311 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1570752
- Blocks: 619226
- Forest area: 141367.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60744
- Scheduled area: 10927.08 ha
- Eligible blocks (age class >= 40): 607439
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.41 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 20.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
