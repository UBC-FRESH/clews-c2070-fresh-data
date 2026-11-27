# WS4 tiled 30-m dataset — K31|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K31|NL|S22` (parent `K31|NL`)
- Tile / row / col: `K31` / 2 / 2
- Province: `NL`
- Centroid: 53.767087, -58.866544
- Allocated harvest: 7497.735806 m3
- Productive subcell area: 119670.480296 ha
- Committed geometry area: 160137.035857 ha
- Clipped inventory geometry: 160137.035857 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1119747
- Blocks: 494926
- Forest area: 100777.23 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40541
- Scheduled area: 8656.11 ha
- Eligible blocks (age class >= 40): 405410
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.06 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 15.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
