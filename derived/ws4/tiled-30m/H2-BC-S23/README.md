# WS4 tiled 30-m dataset — H2|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S23` (parent `H2|BC`)
- Tile / row / col: `H2` / 2 / 3
- Province: `BC`
- Centroid: 50.859742, -126.028232
- Allocated harvest: 154713.713332 m3
- Productive subcell area: 176332.080344 ha
- Committed geometry area: 212475.844362 ha
- Clipped inventory geometry: 212475.844362 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1857532
- Blocks: 999219
- Forest area: 167177.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 95778
- Scheduled area: 14744.88 ha
- Eligible blocks (age class >= 40): 957777
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.31 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 27.45 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
