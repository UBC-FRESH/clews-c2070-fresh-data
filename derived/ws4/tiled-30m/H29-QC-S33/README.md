# WS4 tiled 30-m dataset — H29|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|QC|S33` (parent `H29|QC`)
- Tile / row / col: `H29` / 3 / 3
- Province: `QC`
- Centroid: 51.687166, -65.256877
- Allocated harvest: 33679.138959 m3
- Productive subcell area: 118027.358559 ha
- Committed geometry area: 161863.127054 ha
- Clipped inventory geometry: 161863.127054 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1095481
- Blocks: 503864
- Forest area: 98593.29 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45455
- Scheduled area: 7976.34 ha
- Eligible blocks (age class >= 40): 454548
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.73 MB
- Schedules: 0.53 MB
- Runs: 0.00 MB
- Total: 15.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
