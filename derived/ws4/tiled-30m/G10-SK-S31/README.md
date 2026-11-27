# WS4 tiled 30-m dataset — G10|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|SK|S31` (parent `G10|SK`)
- Tile / row / col: `G10` / 3 / 1
- Province: `SK`
- Centroid: 53.562384, -109.934995
- Allocated harvest: 3370.560254 m3
- Productive subcell area: 14017.511408 ha
- Committed geometry area: 40036.039281 ha
- Clipped inventory geometry: 40036.039281 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 125157
- Blocks: 51139
- Forest area: 11264.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3646
- Scheduled area: 903.06 ha
- Eligible blocks (age class >= 40): 36459
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.07 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 2.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
