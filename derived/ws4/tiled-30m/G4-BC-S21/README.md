# WS4 tiled 30-m dataset — G4|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G4|BC|S21` (parent `G4|BC`)
- Tile / row / col: `G4` / 2 / 1
- Province: `BC`
- Centroid: 50.432652, -122.537067
- Allocated harvest: 114388.707837 m3
- Productive subcell area: 173573.296963 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1693693
- Blocks: 959586
- Forest area: 152432.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89490
- Scheduled area: 13303.26 ha
- Eligible blocks (age class >= 40): 894900
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.37 MB
- Schedules: 1.06 MB
- Runs: 0.00 MB
- Total: 26.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
