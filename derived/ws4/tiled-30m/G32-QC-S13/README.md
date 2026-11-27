# WS4 tiled 30-m dataset — G32|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G32|QC|S13` (parent `G32|QC`)
- Tile / row / col: `G32` / 1 / 3
- Province: `QC`
- Centroid: 47.621149, -61.426396
- Allocated harvest: 626.664745 m3
- Productive subcell area: 1517.598210 ha
- Committed geometry area: 1832.500062 ha
- Clipped inventory geometry: 1832.500062 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 8095
- Blocks: 5065
- Forest area: 728.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4091
- Scheduled area: 602.82 ha
- Eligible blocks (age class >= 40): 4091
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.23 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
