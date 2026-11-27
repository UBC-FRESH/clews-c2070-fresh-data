# WS4 tiled 30-m dataset — K12|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K12|SK|S23` (parent `K12|SK`)
- Tile / row / col: `K12` / 2 / 3
- Province: `SK`
- Centroid: 59.265136, -105.607974
- Allocated harvest: 15924.546966 m3
- Productive subcell area: 142937.039976 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1718570
- Blocks: 324570
- Forest area: 154671.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20923
- Scheduled area: 12334.14 ha
- Eligible blocks (age class >= 40): 209223
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.79 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 16.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
