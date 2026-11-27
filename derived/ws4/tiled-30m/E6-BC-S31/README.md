# WS4 tiled 30-m dataset — E6|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E6|BC|S31` (parent `E6|BC`)
- Tile / row / col: `E6` / 3 / 1
- Province: `BC`
- Centroid: 49.381425, -117.328803
- Allocated harvest: 191461.677037 m3
- Productive subcell area: 207791.088770 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2441645
- Blocks: 1108181
- Forest area: 219748.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 102942
- Scheduled area: 18279.54 ha
- Eligible blocks (age class >= 40): 1029419
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 33.22 MB
- Schedules: 1.23 MB
- Runs: 0.00 MB
- Total: 34.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
