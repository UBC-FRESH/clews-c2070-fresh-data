# WS4 tiled 30-m dataset — J5|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J5|BC|S32` (parent `J5|BC`)
- Tile / row / col: `J5` / 3 / 2
- Province: `BC`
- Centroid: 55.327816, -122.990599
- Allocated harvest: 137778.097846 m3
- Productive subcell area: 216479.315979 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2494529
- Blocks: 1155077
- Forest area: 224507.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 107933
- Scheduled area: 18810.27 ha
- Eligible blocks (age class >= 40): 1079321
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 34.37 MB
- Schedules: 1.30 MB
- Runs: 0.00 MB
- Total: 35.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
