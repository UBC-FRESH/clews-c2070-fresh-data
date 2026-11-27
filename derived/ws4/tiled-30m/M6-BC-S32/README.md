# WS4 tiled 30-m dataset — M6|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M6|BC|S32` (parent `M6|BC`)
- Tile / row / col: `M6` / 3 / 2
- Province: `BC`
- Centroid: 59.657264, -124.011930
- Allocated harvest: 105132.256149 m3
- Productive subcell area: 215827.663959 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2592524
- Blocks: 1217510
- Forest area: 233327.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 115704
- Scheduled area: 20696.22 ha
- Eligible blocks (age class >= 40): 1157038
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 35.68 MB
- Schedules: 1.40 MB
- Runs: 0.00 MB
- Total: 37.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
