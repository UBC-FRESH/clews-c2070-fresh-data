# WS4 tiled 30-m dataset — G14|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G14|MB|S31` (parent `G14|MB`)
- Tile / row / col: `G14` / 3 / 1
- Province: `MB`
- Centroid: 54.491345, -101.071583
- Allocated harvest: 5805.608277 m3
- Productive subcell area: 146461.461203 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2043113
- Blocks: 691007
- Forest area: 183880.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63937
- Scheduled area: 14916.15 ha
- Eligible blocks (age class >= 40): 639364
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.15 MB
- Schedules: 0.76 MB
- Runs: 0.00 MB
- Total: 24.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
