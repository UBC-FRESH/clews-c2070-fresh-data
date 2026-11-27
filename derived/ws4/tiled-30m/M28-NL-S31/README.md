# WS4 tiled 30-m dataset — M28|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M28|NL|S31` (parent `M28|NL`)
- Tile / row / col: `M28` / 3 / 1
- Province: `NL`
- Centroid: 58.836072, -63.263855
- Allocated harvest: 422.694977 m3
- Productive subcell area: 4930.652276 ha
- Committed geometry area: 119310.226518 ha
- Clipped inventory geometry: 119310.226518 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 11329
- Blocks: 7840
- Forest area: 1019.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2554
- Scheduled area: 293.04 ha
- Eligible blocks (age class >= 40): 2554
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.29 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.32 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
