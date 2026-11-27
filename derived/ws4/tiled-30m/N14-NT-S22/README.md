# WS4 tiled 30-m dataset — N14|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N14|NT|S22` (parent `N14|NT`)
- Tile / row / col: `N14` / 2 / 2
- Province: `NT`
- Centroid: 63.701734, -102.270948
- Allocated harvest: 0.248956 m3
- Productive subcell area: 520.161428 ha
- Committed geometry area: 130205.568019 ha
- Clipped inventory geometry: 130205.568019 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2462
- Blocks: 1776
- Forest area: 221.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 579
- Scheduled area: 79.02 ha
- Eligible blocks (age class >= 40): 579
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.12 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
