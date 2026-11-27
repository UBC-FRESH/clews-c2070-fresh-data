# WS4 tiled 30-m dataset — H10|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H10|SK|S12` (parent `H10|SK`)
- Tile / row / col: `H10` / 1 / 2
- Province: `SK`
- Centroid: 54.119721, -109.654745
- Allocated harvest: 43881.003546 m3
- Productive subcell area: 170662.575552 ha
- Committed geometry area: 228993.575601 ha
- Clipped inventory geometry: 228993.575601 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1893843
- Blocks: 579501
- Forest area: 170445.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49576
- Scheduled area: 14766.48 ha
- Eligible blocks (age class >= 40): 495754
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.77 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 22.35 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
