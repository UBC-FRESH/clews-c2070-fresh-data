# WS4 tiled 30-m dataset — I15|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I15|MB|S22` (parent `I15|MB`)
- Tile / row / col: `I15` / 2 / 2
- Province: `MB`
- Centroid: 56.910956, -98.125366
- Allocated harvest: 5439.614180 m3
- Productive subcell area: 170601.009204 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1838993
- Blocks: 392768
- Forest area: 165509.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21812
- Scheduled area: 4913.91 ha
- Eligible blocks (age class >= 40): 218114
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.67 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 17.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
