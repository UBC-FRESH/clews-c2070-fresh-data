# WS4 tiled 30-m dataset — F33|NS|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|NS|S13` (parent `F33|NS`)
- Tile / row / col: `F33` / 1 / 3
- Province: `NS`
- Centroid: 46.015608, -60.645604
- Allocated harvest: 50861.495299 m3
- Productive subcell area: 152429.357126 ha
- Committed geometry area: 177905.258467 ha
- Clipped inventory geometry: 177905.258467 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1739779
- Blocks: 592506
- Forest area: 156580.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52235
- Scheduled area: 13864.50 ha
- Eligible blocks (age class >= 40): 522347
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.82 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 21.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
