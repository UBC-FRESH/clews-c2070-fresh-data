# WS4 tiled 30-m dataset — J33|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J33|QC|S31` (parent `J33|QC`)
- Tile / row / col: `J33` / 3 / 1
- Province: `QC`
- Centroid: 51.730970, -57.127006
- Allocated harvest: 103.415182 m3
- Productive subcell area: 707.542338 ha
- Committed geometry area: 1998.907503 ha
- Clipped inventory geometry: 1998.907503 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5647
- Blocks: 3861
- Forest area: 508.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1794
- Scheduled area: 198.09 ha
- Eligible blocks (age class >= 40): 1794
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.18 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
