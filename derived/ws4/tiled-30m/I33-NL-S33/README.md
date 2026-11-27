# WS4 tiled 30-m dataset — I33|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I33|NL|S33` (parent `I33|NL`)
- Tile / row / col: `I33` / 3 / 3
- Province: `NL`
- Centroid: 50.192558, -56.812056
- Allocated harvest: 7154.009511 m3
- Productive subcell area: 114864.538808 ha
- Committed geometry area: 154656.652438 ha
- Clipped inventory geometry: 154656.652438 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1334008
- Blocks: 795321
- Forest area: 120060.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77737
- Scheduled area: 11900.97 ha
- Eligible blocks (age class >= 40): 777370
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.72 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 21.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
