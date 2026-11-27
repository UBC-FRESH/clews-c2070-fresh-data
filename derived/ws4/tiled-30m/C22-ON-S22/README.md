# WS4 tiled 30-m dataset — C22|ON|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C22|ON|S22` (parent `C22|ON`)
- Tile / row / col: `C22` / 2 / 2
- Province: `ON`
- Centroid: 48.053528, -83.388176
- Allocated harvest: 61578.724163 m3
- Productive subcell area: 223056.778909 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2402635
- Blocks: 784057
- Forest area: 216237.15 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70785
- Scheduled area: 17607.33 ha
- Eligible blocks (age class >= 40): 707842
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.18 MB
- Schedules: 0.84 MB
- Runs: 0.00 MB
- Total: 29.02 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
