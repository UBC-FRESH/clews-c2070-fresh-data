# WS4 tiled 30-m dataset — T7|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T7|NT|S21` (parent `T7|NT`)
- Tile / row / col: `T7` / 2 / 1
- Province: `NT`
- Centroid: 68.141845, -132.721077
- Allocated harvest: 143.457501 m3
- Productive subcell area: 147355.144971 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 971652
- Blocks: 414667
- Forest area: 87448.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30646
- Scheduled area: 5886.90 ha
- Eligible blocks (age class >= 40): 306457
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.72 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 13.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
