# WS4 tiled 30-m dataset — B27|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|QC|S23` (parent `B27|QC`)
- Tile / row / col: `B27` / 2 / 3
- Province: `QC`
- Centroid: 45.080763, -73.887781
- Allocated harvest: 12767.452829 m3
- Productive subcell area: 19699.479353 ha
- Committed geometry area: 90638.896062 ha
- Clipped inventory geometry: 90638.896062 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 605223
- Blocks: 159475
- Forest area: 54470.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11844
- Scheduled area: 3804.75 ha
- Eligible blocks (age class >= 40): 118439
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.14 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 7.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
