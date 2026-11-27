# WS4 tiled 30-m dataset — M28|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S11` (parent `M28|NL`)
- Tile / row / col: `M28` / 1 / 1
- Province: `NL`
- Centroid: 58.093348, -63.919777
- Allocated harvest: 771.927191 m3
- Productive subcell area: 9004.376128 ha
- Committed geometry area: 217884.794017 ha
- Clipped inventory geometry: 217884.794017 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 24599
- Blocks: 14275
- Forest area: 2213.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 806
- Scheduled area: 129.60 ha
- Eligible blocks (age class >= 40): 8056
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.52 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
