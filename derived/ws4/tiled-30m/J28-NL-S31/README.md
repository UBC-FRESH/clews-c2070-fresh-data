# WS4 tiled 30-m dataset — J28|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J28|NL|S31` (parent `J28|NL`)
- Tile / row / col: `J28` / 3 / 1
- Province: `NL`
- Centroid: 55.105322, -66.571626
- Allocated harvest: 1483.248033 m3
- Productive subcell area: 36235.092284 ha
- Committed geometry area: 71991.734473 ha
- Clipped inventory geometry: 71991.734473 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 441894
- Blocks: 257907
- Forest area: 39770.46 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24100
- Scheduled area: 3692.16 ha
- Eligible blocks (age class >= 40): 241000
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.30 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 7.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
