# WS4 tiled 30-m dataset — G21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G21|ON|S31` (parent `G21|ON`)
- Tile / row / col: `G21` / 3 / 1
- Province: `ON`
- Centroid: 54.163075, -84.613260
- Allocated harvest: 7752.746737 m3
- Productive subcell area: 117612.074200 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1321487
- Blocks: 643484
- Forest area: 118933.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53901
- Scheduled area: 11600.55 ha
- Eligible blocks (age class >= 40): 539007
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.43 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 19.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
