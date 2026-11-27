# WS4 tiled 30-m dataset — I35|NL|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I35|NL|S32` (parent `I35|NL`)
- Tile / row / col: `I35` / 3 / 2
- Province: `NL`
- Centroid: 48.837723, -53.988801
- Allocated harvest: 7471.126590 m3
- Productive subcell area: 97939.361315 ha
- Committed geometry area: 150434.154823 ha
- Clipped inventory geometry: 150434.154823 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1397167
- Blocks: 587829
- Forest area: 125745.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 55859
- Scheduled area: 11501.19 ha
- Eligible blocks (age class >= 40): 558581
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.73 MB
- Schedules: 0.66 MB
- Runs: 0.00 MB
- Total: 19.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
