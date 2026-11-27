# WS4 tiled 30-m dataset — M8|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S23` (parent `M8|NT`)
- Tile / row / col: `M8` / 2 / 3
- Province: `NT`
- Centroid: 60.512230, -117.700934
- Allocated harvest: 154.254008 m3
- Productive subcell area: 110912.963160 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1346522
- Blocks: 532018
- Forest area: 121186.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45933
- Scheduled area: 9648.90 ha
- Eligible blocks (age class >= 40): 459329
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.45 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 18.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
