# WS4 tiled 30-m dataset — K33|NL|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K33|NL|S21` (parent `K33|NL`)
- Tile / row / col: `K33` / 2 / 1
- Province: `NL`
- Centroid: 52.498539, -55.954739
- Allocated harvest: 3343.881156 m3
- Productive subcell area: 76592.323550 ha
- Committed geometry area: 118351.064152 ha
- Clipped inventory geometry: 118351.064152 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 826092
- Blocks: 393658
- Forest area: 74348.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32718
- Scheduled area: 6248.16 ha
- Eligible blocks (age class >= 40): 327175
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.54 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 11.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
