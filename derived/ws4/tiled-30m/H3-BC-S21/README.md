# WS4 tiled 30-m dataset — H3|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S21` (parent `H3|BC`)
- Tile / row / col: `H3` / 2 / 1
- Province: `BC`
- Centroid: 51.058503, -125.390778
- Allocated harvest: 87707.576188 m3
- Productive subcell area: 133095.592656 ha
- Committed geometry area: 238937.722648 ha
- Clipped inventory geometry: 238937.722648 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1127251
- Blocks: 668412
- Forest area: 101452.59 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 60822
- Scheduled area: 8257.23 ha
- Eligible blocks (age class >= 40): 608220
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.16 MB
- Schedules: 0.72 MB
- Runs: 0.00 MB
- Total: 17.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
