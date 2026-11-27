# WS4 tiled 30-m dataset — I29|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I29|NL|S13` (parent `I29|NL`)
- Tile / row / col: `I29` / 1 / 3
- Province: `NL`
- Centroid: 52.159560, -64.863872
- Allocated harvest: 7442.226337 m3
- Productive subcell area: 140684.773662 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2040181
- Blocks: 895945
- Forest area: 183616.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84581
- Scheduled area: 17146.89 ha
- Eligible blocks (age class >= 40): 845807
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.44 MB
- Schedules: 1.00 MB
- Runs: 0.00 MB
- Total: 27.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
