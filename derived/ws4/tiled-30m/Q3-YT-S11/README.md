# WS4 tiled 30-m dataset — Q3|YT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q3|YT|S11` (parent `Q3|YT`)
- Tile / row / col: `Q3` / 1 / 1
- Province: `YT`
- Centroid: 61.141354, -136.894634
- Allocated harvest: 255.809910 m3
- Productive subcell area: 171969.252036 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1522165
- Blocks: 662860
- Forest area: 136994.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55438
- Scheduled area: 11313.63 ha
- Eligible blocks (age class >= 40): 554373
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.39 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 21.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
