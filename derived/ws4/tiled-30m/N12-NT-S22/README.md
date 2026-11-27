# WS4 tiled 30-m dataset — N12|NT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N12|NT|S22` (parent `N12|NT`)
- Tile / row / col: `N12` / 2 / 2
- Province: `NT`
- Centroid: 63.267027, -108.155919
- Allocated harvest: 17.062886 m3
- Productive subcell area: 34698.322056 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 186085
- Blocks: 97543
- Forest area: 16747.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5214
- Scheduled area: 725.85 ha
- Eligible blocks (age class >= 40): 52132
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.35 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
