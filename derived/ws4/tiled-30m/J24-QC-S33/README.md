# WS4 tiled 30-m dataset — J24|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J24|QC|S33` (parent `J24|QC`)
- Tile / row / col: `J24` / 3 / 3
- Province: `QC`
- Centroid: 56.950762, -74.206219
- Allocated harvest: 10709.596663 m3
- Productive subcell area: 64489.195964 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 285942
- Blocks: 192673
- Forest area: 25734.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11024
- Scheduled area: 1467.81 ha
- Eligible blocks (age class >= 40): 110233
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.28 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 5.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
