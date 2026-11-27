# WS4 tiled 30-m dataset — H13|SK|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S11` (parent `H13|SK`)
- Tile / row / col: `H13` / 1 / 1
- Province: `SK`
- Centroid: 54.788842, -103.512303
- Allocated harvest: 32942.635155 m3
- Productive subcell area: 180395.801396 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1922739
- Blocks: 584154
- Forest area: 173046.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51952
- Scheduled area: 11622.69 ha
- Eligible blocks (age class >= 40): 519515
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.60 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 22.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
