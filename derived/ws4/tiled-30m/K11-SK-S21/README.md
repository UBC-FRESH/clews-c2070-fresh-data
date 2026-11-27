# WS4 tiled 30-m dataset — K11|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|SK|S21` (parent `K11|SK`)
- Tile / row / col: `K11` / 2 / 1
- Province: `SK`
- Centroid: 58.812031, -109.776134
- Allocated harvest: 7058.709792 m3
- Productive subcell area: 69880.509425 ha
- Committed geometry area: 127340.643766 ha
- Clipped inventory geometry: 127340.643766 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1082937
- Blocks: 286950
- Forest area: 97464.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26490
- Scheduled area: 8800.11 ha
- Eligible blocks (age class >= 40): 264900
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.58 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 11.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
