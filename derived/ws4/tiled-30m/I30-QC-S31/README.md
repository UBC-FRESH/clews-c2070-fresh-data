# WS4 tiled 30-m dataset — I30|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|QC|S31` (parent `I30|QC`)
- Tile / row / col: `I30` / 3 / 1
- Province: `QC`
- Centroid: 52.705744, -63.716754
- Allocated harvest: 9150.907313 m3
- Productive subcell area: 40534.981324 ha
- Committed geometry area: 52952.651373 ha
- Clipped inventory geometry: 52952.651373 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 461449
- Blocks: 119627
- Forest area: 41530.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11054
- Scheduled area: 4111.47 ha
- Eligible blocks (age class >= 40): 110533
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.58 MB
- Schedules: 0.12 MB
- Runs: 0.00 MB
- Total: 5.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
