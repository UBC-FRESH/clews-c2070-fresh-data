# WS4 tiled 30-m dataset — I33|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I33|NL|S32` (parent `I33|NL`)
- Tile / row / col: `I33` / 3 / 2
- Province: `NL`
- Centroid: 50.380956, -57.212688
- Allocated harvest: 9015.572798 m3
- Productive subcell area: 144753.737040 ha
- Committed geometry area: 194900.259304 ha
- Clipped inventory geometry: 194900.259304 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1630753
- Blocks: 921899
- Forest area: 146767.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87482
- Scheduled area: 13526.91 ha
- Eligible blocks (age class >= 40): 874820
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.36 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 25.40 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
