# WS4 tiled 30-m dataset — H33|NL|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H33|NL|S12` (parent `H33|NL`)
- Tile / row / col: `H33` / 1 / 2
- Province: `NL`
- Centroid: 48.560965, -59.022541
- Allocated harvest: 1718.628153 m3
- Productive subcell area: 24699.106111 ha
- Committed geometry area: 35692.597058 ha
- Clipped inventory geometry: 35692.597058 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 325190
- Blocks: 147340
- Forest area: 29267.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13262
- Scheduled area: 2640.51 ha
- Eligible blocks (age class >= 40): 132618
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.22 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 5.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
