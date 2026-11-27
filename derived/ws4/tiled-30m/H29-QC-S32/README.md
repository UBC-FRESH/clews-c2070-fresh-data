# WS4 tiled 30-m dataset — H29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|QC|S32` (parent `H29|QC`)
- Tile / row / col: `H29` / 3 / 2
- Province: `QC`
- Centroid: 51.912212, -65.869798
- Allocated harvest: 40956.032417 m3
- Productive subcell area: 143528.975878 ha
- Committed geometry area: 196836.133098 ha
- Clipped inventory geometry: 196836.133098 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1522446
- Blocks: 811520
- Forest area: 137020.14 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76397
- Scheduled area: 12271.95 ha
- Eligible blocks (age class >= 40): 763969
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.71 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 22.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
