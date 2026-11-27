# WS4 tiled 30-m dataset — C31|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C31|NB|S31` (parent `C31|NB`)
- Tile / row / col: `C31` / 3 / 1
- Province: `NB`
- Centroid: 45.169656, -67.335208
- Allocated harvest: 12268.933766 m3
- Productive subcell area: 15148.318485 ha
- Committed geometry area: 16954.230808 ha
- Clipped inventory geometry: 16954.230808 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 154201
- Blocks: 67763
- Forest area: 13878.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5730
- Scheduled area: 1102.14 ha
- Eligible blocks (age class >= 40): 57294
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.61 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
