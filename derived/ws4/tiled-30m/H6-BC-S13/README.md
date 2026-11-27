# WS4 tiled 30-m dataset — H6|BC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S13` (parent `H6|BC`)
- Tile / row / col: `H6` / 1 / 3
- Province: `BC`
- Centroid: 52.424716, -117.918906
- Allocated harvest: 2361.897460 m3
- Productive subcell area: 4004.634767 ha
- Committed geometry area: 6732.541985 ha
- Clipped inventory geometry: 6732.541985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 19570
- Blocks: 12085
- Forest area: 1761.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1087
- Scheduled area: 156.87 ha
- Eligible blocks (age class >= 40): 10861
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.46 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
