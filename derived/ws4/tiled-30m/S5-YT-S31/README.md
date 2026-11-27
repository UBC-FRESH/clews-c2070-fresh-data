# WS4 tiled 30-m dataset — S5|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `S5|YT|S31` (parent `S5|YT`)
- Tile / row / col: `S5` / 3 / 1
- Province: `YT`
- Centroid: 65.765974, -137.065163
- Allocated harvest: 200.402540 m3
- Productive subcell area: 134571.201402 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1505047
- Blocks: 612060
- Forest area: 135454.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44410
- Scheduled area: 8278.65 ha
- Eligible blocks (age class >= 40): 444094
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.41 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 19.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
