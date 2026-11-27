# WS4 tiled 30-m dataset — B26|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|ON|S21` (parent `B26|ON`)
- Tile / row / col: `B26` / 2 / 1
- Province: `ON`
- Centroid: 45.585824, -76.928048
- Allocated harvest: 48138.199210 m3
- Productive subcell area: 159308.762624 ha
- Committed geometry area: 200394.745486 ha
- Clipped inventory geometry: 200394.745486 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1223852
- Blocks: 485543
- Forest area: 110146.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42152
- Scheduled area: 9544.68 ha
- Eligible blocks (age class >= 40): 421517
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.14 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 16.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
