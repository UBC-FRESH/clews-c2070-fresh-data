# WS4 tiled 30-m dataset — B29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B29|QC|S31` (parent `B29|QC`)
- Tile / row / col: `B29` / 3 / 1
- Province: `QC`
- Centroid: 45.021567, -71.518706
- Allocated harvest: 374.971868 m3
- Productive subcell area: 618.038385 ha
- Committed geometry area: 539.342493 ha
- Clipped inventory geometry: 539.342493 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5666
- Blocks: 1524
- Forest area: 509.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1414
- Scheduled area: 442.44 ha
- Eligible blocks (age class >= 40): 1414
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.14 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.16 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
