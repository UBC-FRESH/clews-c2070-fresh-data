# WS4 tiled 30-m dataset — L7|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S13` (parent `L7|AB`)
- Tile / row / col: `L7` / 1 / 3
- Province: `AB`
- Centroid: 58.293148, -118.937708
- Allocated harvest: 119245.075069 m3
- Productive subcell area: 211197.288575 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2257365
- Blocks: 913775
- Forest area: 203162.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 81417
- Scheduled area: 16615.35 ha
- Eligible blocks (age class >= 40): 814164
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.73 MB
- Schedules: 0.97 MB
- Runs: 0.00 MB
- Total: 29.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
