# WS4 tiled 30-m dataset — H13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S33` (parent `H13|SK`)
- Tile / row / col: `H13` / 3 / 3
- Province: `SK`
- Centroid: 55.803812, -102.252569
- Allocated harvest: 21780.731137 m3
- Productive subcell area: 119272.560621 ha
- Committed geometry area: 165292.872253 ha
- Clipped inventory geometry: 165292.872253 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1536148
- Blocks: 345278
- Forest area: 138253.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23887
- Scheduled area: 4815.81 ha
- Eligible blocks (age class >= 40): 238865
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.38 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 15.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
