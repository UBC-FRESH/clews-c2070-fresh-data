# WS4 tiled 30-m dataset — K25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K25|QC|S32` (parent `K25|QC`)
- Tile / row / col: `K25` / 3 / 2
- Province: `QC`
- Centroid: 57.936807, -71.731851
- Allocated harvest: 5937.457941 m3
- Productive subcell area: 38802.265166 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 56401
- Blocks: 36708
- Forest area: 5076.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1137
- Scheduled area: 142.65 ha
- Eligible blocks (age class >= 40): 11364
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.19 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 1.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
