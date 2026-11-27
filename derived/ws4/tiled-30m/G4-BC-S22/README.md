# WS4 tiled 30-m dataset — G4|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G4|BC|S22` (parent `G4|BC`)
- Tile / row / col: `G4` / 2 / 2
- Province: `BC`
- Centroid: 50.620212, -121.891871
- Allocated harvest: 114388.707837 m3
- Productive subcell area: 173573.296963 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2011736
- Blocks: 1003485
- Forest area: 181056.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 93333
- Scheduled area: 15080.94 ha
- Eligible blocks (age class >= 40): 933325
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.37 MB
- Schedules: 1.11 MB
- Runs: 0.00 MB
- Total: 29.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
