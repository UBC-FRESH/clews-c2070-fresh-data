# WS4 tiled 30-m dataset — H31|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S21` (parent `H31|QC`)
- Tile / row / col: `H31` / 2 / 1
- Province: `QC`
- Centroid: 50.519314, -62.991101
- Allocated harvest: 52871.869322 m3
- Productive subcell area: 171791.015112 ha
- Committed geometry area: 239233.244102 ha
- Clipped inventory geometry: 239233.244102 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1427087
- Blocks: 562030
- Forest area: 128437.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 47039
- Scheduled area: 10978.65 ha
- Eligible blocks (age class >= 40): 470386
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.38 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 18.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
