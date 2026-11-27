# WS4 tiled 30-m dataset — G32|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G32|QC|S31` (parent `G32|QC`)
- Tile / row / col: `G32` / 3 / 1
- Province: `QC`
- Centroid: 49.181239, -61.940131
- Allocated harvest: 26464.757569 m3
- Productive subcell area: 64089.880666 ha
- Committed geometry area: 77388.540361 ha
- Clipped inventory geometry: 77388.540361 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 548473
- Blocks: 316460
- Forest area: 49362.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27719
- Scheduled area: 4353.30 ha
- Eligible blocks (age class >= 40): 277184
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.79 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 9.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
