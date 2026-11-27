# WS4 tiled 30-m dataset — L26|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S12` (parent `L26|QC`)
- Tile / row / col: `L26` / 1 / 2
- Province: `QC`
- Centroid: 57.841473, -69.003715
- Allocated harvest: 16243.331689 m3
- Productive subcell area: 92979.868016 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1466412
- Blocks: 806981
- Forest area: 131977.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65975
- Scheduled area: 10047.24 ha
- Eligible blocks (age class >= 40): 659745
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.51 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 22.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
