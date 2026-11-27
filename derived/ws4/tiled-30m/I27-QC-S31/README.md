# WS4 tiled 30-m dataset — I27|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I27|QC|S31` (parent `I27|QC`)
- Tile / row / col: `I27` / 3 / 1
- Province: `QC`
- Centroid: 54.526222, -69.748024
- Allocated harvest: 17088.057852 m3
- Productive subcell area: 130072.193185 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 977174
- Blocks: 321540
- Forest area: 87945.66 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 27569
- Scheduled area: 7547.13 ha
- Eligible blocks (age class >= 40): 275688
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.68 MB
- Schedules: 0.32 MB
- Runs: 0.00 MB
- Total: 12.00 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
