# WS4 tiled 30-m dataset — F21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F21|ON|S31` (parent `F21|ON`)
- Tile / row / col: `F21` / 3 / 1
- Province: `ON`
- Centroid: 52.812410, -84.979696
- Allocated harvest: 9105.239574 m3
- Productive subcell area: 122428.732512 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1281716
- Blocks: 469868
- Forest area: 115354.44 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42786
- Scheduled area: 10499.13 ha
- Eligible blocks (age class >= 40): 427855
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.10 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 16.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
