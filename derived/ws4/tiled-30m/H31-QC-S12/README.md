# WS4 tiled 30-m dataset — H31|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S12` (parent `H31|QC`)
- Tile / row / col: `H31` / 1 / 2
- Province: `QC`
- Centroid: 49.651593, -62.732808
- Allocated harvest: 858.500615 m3
- Productive subcell area: 2789.435934 ha
- Committed geometry area: 3884.521010 ha
- Clipped inventory geometry: 3884.521010 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 39305
- Blocks: 19632
- Forest area: 3537.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1925
- Scheduled area: 358.38 ha
- Eligible blocks (age class >= 40): 19242
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.77 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
