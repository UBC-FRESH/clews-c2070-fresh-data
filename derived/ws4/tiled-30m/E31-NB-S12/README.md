# WS4 tiled 30-m dataset — E31|NB|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S12` (parent `E31|NB`)
- Tile / row / col: `E31` / 1 / 2
- Province: `NB`
- Centroid: 46.327345, -65.522652
- Allocated harvest: 181448.863957 m3
- Productive subcell area: 226598.170928 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2655680
- Blocks: 909592
- Forest area: 239011.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72898
- Scheduled area: 15242.58 ha
- Eligible blocks (age class >= 40): 728976
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.26 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 32.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
