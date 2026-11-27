# WS4 tiled 30-m dataset — E24|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E24|QC|S22` (parent `E24|QC`)
- Tile / row / col: `E24` / 2 / 2
- Province: `QC`
- Centroid: 50.095714, -78.479018
- Allocated harvest: 35482.439363 m3
- Productive subcell area: 174007.072475 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1722333
- Blocks: 606361
- Forest area: 155009.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50919
- Scheduled area: 12385.53 ha
- Eligible blocks (age class >= 40): 509188
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.95 MB
- Schedules: 0.60 MB
- Runs: 0.00 MB
- Total: 21.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
