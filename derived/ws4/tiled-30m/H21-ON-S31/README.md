# WS4 tiled 30-m dataset — H21|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H21|ON|S31` (parent `H21|ON`)
- Tile / row / col: `H21` / 3 / 1
- Province: `ON`
- Centroid: 55.273967, -83.937745
- Allocated harvest: 43.680837 m3
- Productive subcell area: 806.556609 ha
- Committed geometry area: 2643.555003 ha
- Clipped inventory geometry: 2643.555003 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2226
- Blocks: 1520
- Forest area: 200.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1225
- Scheduled area: 165.42 ha
- Eligible blocks (age class >= 40): 1225
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.11 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
