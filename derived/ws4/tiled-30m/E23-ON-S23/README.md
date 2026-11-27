# WS4 tiled 30-m dataset — E23|ON|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|ON|S23` (parent `E23|ON`)
- Tile / row / col: `E23` / 2 / 3
- Province: `ON`
- Centroid: 50.314355, -79.859686
- Allocated harvest: 23623.940836 m3
- Productive subcell area: 197863.533129 ha
- Committed geometry area: 238739.256099 ha
- Clipped inventory geometry: 238739.256099 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2018698
- Blocks: 829989
- Forest area: 181682.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76727
- Scheduled area: 15942.78 ha
- Eligible blocks (age class >= 40): 767267
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.60 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 26.51 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
