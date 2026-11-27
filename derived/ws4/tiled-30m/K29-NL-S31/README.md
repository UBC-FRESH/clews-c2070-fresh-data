# WS4 tiled 30-m dataset — K29|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S31` (parent `K29|NL`)
- Tile / row / col: `K29` / 3 / 1
- Province: `NL`
- Centroid: 55.816509, -63.314596
- Allocated harvest: 5278.824649 m3
- Productive subcell area: 110308.250186 ha
- Committed geometry area: 234221.632266 ha
- Clipped inventory geometry: 234221.632266 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 674496
- Blocks: 348378
- Forest area: 60704.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22998
- Scheduled area: 3535.65 ha
- Eligible blocks (age class >= 40): 229974
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.94 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 10.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
