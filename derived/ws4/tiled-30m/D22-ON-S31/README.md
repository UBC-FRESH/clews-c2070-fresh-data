# WS4 tiled 30-m dataset — D22|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D22|ON|S31` (parent `D22|ON`)
- Tile / row / col: `D22` / 3 / 1
- Province: `ON`
- Centroid: 49.903296, -83.567797
- Allocated harvest: 49456.255781 m3
- Productive subcell area: 231072.091541 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2527148
- Blocks: 896412
- Forest area: 227443.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 83074
- Scheduled area: 20916.90 ha
- Eligible blocks (age class >= 40): 830739
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.91 MB
- Schedules: 0.99 MB
- Runs: 0.00 MB
- Total: 31.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
