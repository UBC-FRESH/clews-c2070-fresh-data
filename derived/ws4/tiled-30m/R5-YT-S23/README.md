# WS4 tiled 30-m dataset — R5|YT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R5|YT|S23` (parent `R5|YT`)
- Tile / row / col: `R5` / 2 / 3
- Province: `YT`
- Centroid: 64.799914, -132.779830
- Allocated harvest: 72.794051 m3
- Productive subcell area: 64725.993993 ha
- Committed geometry area: 200077.414536 ha
- Clipped inventory geometry: 200077.414536 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 240849
- Blocks: 128161
- Forest area: 21676.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8608
- Scheduled area: 1439.01 ha
- Eligible blocks (age class >= 40): 86073
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.35 MB
- Schedules: 0.10 MB
- Runs: 0.00 MB
- Total: 4.44 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
