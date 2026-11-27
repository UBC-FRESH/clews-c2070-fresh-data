# WS4 tiled 30-m dataset — D20|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D20|ON|S31` (parent `D20|ON`)
- Tile / row / col: `D20` / 3 / 1
- Province: `ON`
- Centroid: 50.300154, -87.733695
- Allocated harvest: 48678.315136 m3
- Productive subcell area: 212302.677765 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2522358
- Blocks: 976253
- Forest area: 227012.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 88210
- Scheduled area: 18325.26 ha
- Eligible blocks (age class >= 40): 882094
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.84 MB
- Schedules: 1.05 MB
- Runs: 0.00 MB
- Total: 32.89 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
