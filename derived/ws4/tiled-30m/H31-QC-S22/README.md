# WS4 tiled 30-m dataset — H31|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S22` (parent `H31|QC`)
- Tile / row / col: `H31` / 2 / 2
- Province: `QC`
- Centroid: 50.379669, -62.336749
- Allocated harvest: 31860.148545 m3
- Productive subcell area: 103519.836358 ha
- Committed geometry area: 144159.962409 ha
- Clipped inventory geometry: 144159.962409 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 851470
- Blocks: 348062
- Forest area: 76632.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29593
- Scheduled area: 6988.05 ha
- Eligible blocks (age class >= 40): 295923
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.30 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 11.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
