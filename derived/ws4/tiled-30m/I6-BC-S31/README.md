# WS4 tiled 30-m dataset — I6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|BC|S31` (parent `I6|BC`)
- Tile / row / col: `I6` / 3 / 1
- Province: `BC`
- Centroid: 54.448606, -120.567744
- Allocated harvest: 118820.983725 m3
- Productive subcell area: 189497.874768 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2040403
- Blocks: 854967
- Forest area: 183636.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78329
- Scheduled area: 14755.50 ha
- Eligible blocks (age class >= 40): 783287
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.29 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 27.22 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
