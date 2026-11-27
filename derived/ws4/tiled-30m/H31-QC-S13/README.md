# WS4 tiled 30-m dataset — H31|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S13` (parent `H31|QC`)
- Tile / row / col: `H31` / 1 / 3
- Province: `QC`
- Centroid: 49.575499, -62.519545
- Allocated harvest: 364.693219 m3
- Productive subcell area: 1184.959395 ha
- Committed geometry area: 1650.154287 ha
- Clipped inventory geometry: 1650.154287 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 17403
- Blocks: 9052
- Forest area: 1566.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 896
- Scheduled area: 180.63 ha
- Eligible blocks (age class >= 40): 8955
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.38 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
