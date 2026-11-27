# WS4 tiled 30-m dataset — J15|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J15|MB|S22` (parent `J15|MB`)
- Tile / row / col: `J15` / 2 / 2
- Province: `MB`
- Centroid: 58.289765, -98.254274
- Allocated harvest: 3228.639423 m3
- Productive subcell area: 155253.293299 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1669561
- Blocks: 428983
- Forest area: 150260.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29806
- Scheduled area: 8329.32 ha
- Eligible blocks (age class >= 40): 298055
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.94 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 18.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
