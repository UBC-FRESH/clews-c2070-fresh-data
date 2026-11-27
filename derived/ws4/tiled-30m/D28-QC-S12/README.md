# WS4 tiled 30-m dataset — D28|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D28|QC|S12` (parent `D28|QC`)
- Tile / row / col: `D28` / 1 / 2
- Province: `QC`
- Centroid: 46.727876, -71.612823
- Allocated harvest: 106237.283055 m3
- Productive subcell area: 181163.254800 ha
- Committed geometry area: 228686.316891 ha
- Clipped inventory geometry: 228686.316891 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1437210
- Blocks: 502269
- Forest area: 129348.90 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42316
- Scheduled area: 10914.12 ha
- Eligible blocks (age class >= 40): 423155
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.73 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 18.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
