# WS4 tiled 30-m dataset — I30|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I30|NL|S11` (parent `I30|NL`)
- Tile / row / col: `I30` / 1 / 1
- Province: `NL`
- Centroid: 51.988338, -64.393231
- Allocated harvest: 4878.373949 m3
- Productive subcell area: 74409.580035 ha
- Committed geometry area: 100942.149358 ha
- Clipped inventory geometry: 100942.149358 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 669191
- Blocks: 319637
- Forest area: 60227.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28484
- Scheduled area: 5288.22 ha
- Eligible blocks (age class >= 40): 284839
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.52 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 9.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
