# WS4 tiled 30-m dataset — F24|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F24|QC|S21` (parent `F24|QC`)
- Tile / row / col: `F24` / 2 / 1
- Province: `QC`
- Centroid: 51.527385, -78.578770
- Allocated harvest: 27022.633999 m3
- Productive subcell area: 132524.756069 ha
- Committed geometry area: 217121.385436 ha
- Clipped inventory geometry: 217121.385436 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1578063
- Blocks: 594512
- Forest area: 142025.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55644
- Scheduled area: 13045.59 ha
- Eligible blocks (age class >= 40): 556433
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.02 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 20.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
