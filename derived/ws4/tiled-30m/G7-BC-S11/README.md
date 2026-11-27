# WS4 tiled 30-m dataset — G7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|BC|S11` (parent `G7|BC`)
- Tile / row / col: `G7` / 1 / 1
- Province: `BC`
- Centroid: 51.468194, -116.497274
- Allocated harvest: 29055.199122 m3
- Productive subcell area: 44363.007868 ha
- Committed geometry area: 79663.488055 ha
- Clipped inventory geometry: 79663.488055 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 377899
- Blocks: 209805
- Forest area: 34010.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19843
- Scheduled area: 3122.73 ha
- Eligible blocks (age class >= 40): 198429
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.34 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 6.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
