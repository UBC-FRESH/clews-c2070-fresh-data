# WS4 tiled 30-m dataset — I6|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I6|BC|S21` (parent `I6|BC`)
- Tile / row / col: `I6` / 2 / 1
- Province: `BC`
- Centroid: 54.032040, -120.319639
- Allocated harvest: 102397.340265 m3
- Productive subcell area: 163305.148246 ha
- Committed geometry area: 215444.564281 ha
- Clipped inventory geometry: 215444.564281 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1418855
- Blocks: 710985
- Forest area: 127696.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66919
- Scheduled area: 11716.02 ha
- Eligible blocks (age class >= 40): 669186
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.10 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 20.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
