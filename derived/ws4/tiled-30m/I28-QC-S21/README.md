# WS4 tiled 30-m dataset — I28|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|QC|S21` (parent `I28|QC`)
- Tile / row / col: `I28` / 2 / 1
- Province: `QC`
- Centroid: 53.559613, -67.924302
- Allocated harvest: 22719.334555 m3
- Productive subcell area: 148027.233473 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1682907
- Blocks: 480388
- Forest area: 151461.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 44677
- Scheduled area: 14437.89 ha
- Eligible blocks (age class >= 40): 446761
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.98 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 19.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
