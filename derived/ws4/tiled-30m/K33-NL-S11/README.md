# WS4 tiled 30-m dataset — K33|NL|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K33|NL|S11` (parent `K33|NL`)
- Tile / row / col: `K33` / 1 / 1
- Province: `NL`
- Centroid: 52.153501, -56.243512
- Allocated harvest: 7040.648137 m3
- Productive subcell area: 161267.573516 ha
- Committed geometry area: 249191.930131 ha
- Clipped inventory geometry: 249191.930131 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2037141
- Blocks: 840210
- Forest area: 183342.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75529
- Scheduled area: 16317.81 ha
- Eligible blocks (age class >= 40): 755290
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.07 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 26.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
