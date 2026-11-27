# WS4 tiled 30-m dataset — I28|NL|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I28|NL|S13` (parent `I28|NL`)
- Tile / row / col: `I28` / 1 / 3
- Province: `NL`
- Centroid: 52.879631, -66.895547
- Allocated harvest: 2202.835185 m3
- Productive subcell area: 49539.475413 ha
- Committed geometry area: 93075.519546 ha
- Clipped inventory geometry: 93075.519546 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 678809
- Blocks: 256242
- Forest area: 61092.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22688
- Scheduled area: 5043.96 ha
- Eligible blocks (age class >= 40): 226875
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.77 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 9.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
