# WS4 tiled 30-m dataset — H29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|QC|S31` (parent `H29|QC`)
- Tile / row / col: `H29` / 3 / 1
- Province: `QC`
- Centroid: 52.138385, -66.553655
- Allocated harvest: 44567.809019 m3
- Productive subcell area: 156186.320014 ha
- Committed geometry area: 214194.458550 ha
- Clipped inventory geometry: 214194.458550 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1246562
- Blocks: 462013
- Forest area: 112190.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37423
- Scheduled area: 7653.15 ha
- Eligible blocks (age class >= 40): 374229
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.46 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 15.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
