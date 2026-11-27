# WS4 tiled 30-m dataset — I36|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I36|NL|S11` (parent `I36|NL`)
- Tile / row / col: `I36` / 1 / 1
- Province: `NL`
- Centroid: 47.525509, -53.596753
- Allocated harvest: 9231.998608 m3
- Productive subcell area: 113770.443080 ha
- Committed geometry area: 163611.981428 ha
- Clipped inventory geometry: 163611.981428 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1378433
- Blocks: 629040
- Forest area: 124058.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58165
- Scheduled area: 11469.87 ha
- Eligible blocks (age class >= 40): 581648
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.02 MB
- Schedules: 0.69 MB
- Runs: 0.00 MB
- Total: 19.71 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
