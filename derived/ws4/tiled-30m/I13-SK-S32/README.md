# WS4 tiled 30-m dataset — I13|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I13|SK|S32` (parent `I13|SK`)
- Tile / row / col: `I13` / 3 / 2
- Province: `SK`
- Centroid: 57.122942, -103.238478
- Allocated harvest: 27419.892255 m3
- Productive subcell area: 171206.562836 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2072789
- Blocks: 278817
- Forest area: 186551.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17676
- Scheduled area: 7197.30 ha
- Eligible blocks (age class >= 40): 176756
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.93 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 17.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
