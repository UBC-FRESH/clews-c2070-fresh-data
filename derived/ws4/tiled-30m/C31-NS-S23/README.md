# WS4 tiled 30-m dataset — C31|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C31|NS|S23` (parent `C31|NS`)
- Tile / row / col: `C31` / 2 / 3
- Province: `NS`
- Centroid: 44.163654, -66.107635
- Allocated harvest: 22468.915267 m3
- Productive subcell area: 40148.418942 ha
- Committed geometry area: 48868.161941 ha
- Clipped inventory geometry: 48868.161941 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 415816
- Blocks: 141953
- Forest area: 37423.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11704
- Scheduled area: 2975.85 ha
- Eligible blocks (age class >= 40): 117037
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.69 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.82 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
