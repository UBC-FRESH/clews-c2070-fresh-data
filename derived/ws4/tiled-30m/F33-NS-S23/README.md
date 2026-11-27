# WS4 tiled 30-m dataset — F33|NS|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|NS|S23` (parent `F33|NS`)
- Tile / row / col: `F33` / 2 / 3
- Province: `NS`
- Centroid: 46.447318, -60.551929
- Allocated harvest: 32589.801886 m3
- Productive subcell area: 97670.005987 ha
- Committed geometry area: 113993.839423 ha
- Clipped inventory geometry: 113993.839423 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1070532
- Blocks: 392782
- Forest area: 96347.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35991
- Scheduled area: 10368.09 ha
- Eligible blocks (age class >= 40): 359904
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.29 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 13.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
