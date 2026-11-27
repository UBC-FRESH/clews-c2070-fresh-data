# WS4 tiled 30-m dataset — I3|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I3|BC|S32` (parent `I3|BC`)
- Tile / row / col: `I3` / 3 / 2
- Province: `BC`
- Centroid: 52.873926, -126.115106
- Allocated harvest: 88119.082702 m3
- Productive subcell area: 179352.040200 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2357215
- Blocks: 723683
- Forest area: 212149.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62717
- Scheduled area: 9805.41 ha
- Eligible blocks (age class >= 40): 627161
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.91 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 26.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
