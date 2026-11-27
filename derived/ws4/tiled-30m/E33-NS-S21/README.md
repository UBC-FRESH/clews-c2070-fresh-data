# WS4 tiled 30-m dataset — E33|NS|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S21` (parent `E33|NS`)
- Tile / row / col: `E33` / 2 / 1
- Province: `NS`
- Centroid: 45.595904, -62.385645
- Allocated harvest: 57141.773006 m3
- Productive subcell area: 118890.614026 ha
- Committed geometry area: 143406.500357 ha
- Clipped inventory geometry: 143406.500357 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1288924
- Blocks: 464733
- Forest area: 116003.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36442
- Scheduled area: 7465.23 ha
- Eligible blocks (age class >= 40): 364419
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.07 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 16.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
