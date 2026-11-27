# WS4 tiled 30-m dataset — L31|NL|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L31|NL|S22` (parent `L31|NL`)
- Tile / row / col: `L31` / 2 / 2
- Province: `NL`
- Centroid: 54.840446, -57.986730
- Allocated harvest: 487.435134 m3
- Productive subcell area: 8218.893923 ha
- Committed geometry area: 14788.163817 ha
- Clipped inventory geometry: 14788.163817 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 49173
- Blocks: 22702
- Forest area: 4425.57 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1130
- Scheduled area: 166.68 ha
- Eligible blocks (age class >= 40): 11299
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.89 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.90 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
