# WS4 tiled 30-m dataset — D17|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D17|ON|S11` (parent `D17|ON`)
- Tile / row / col: `D17` / 1 / 1
- Province: `ON`
- Centroid: 49.670437, -94.082320
- Allocated harvest: 39747.682994 m3
- Productive subcell area: 171942.883232 ha
- Committed geometry area: 223369.576838 ha
- Clipped inventory geometry: 223369.576838 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1860308
- Blocks: 772430
- Forest area: 167427.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 72764
- Scheduled area: 14477.31 ha
- Eligible blocks (age class >= 40): 727638
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.85 MB
- Schedules: 0.86 MB
- Runs: 0.00 MB
- Total: 24.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
