# WS4 tiled 30-m dataset — H13|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H13|SK|S22` (parent `H13|SK`)
- Tile / row / col: `H13` / 2 / 2
- Province: `SK`
- Centroid: 55.301566, -102.823599
- Allocated harvest: 32942.635155 m3
- Productive subcell area: 180395.801396 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1754850
- Blocks: 389491
- Forest area: 157936.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19899
- Scheduled area: 3124.71 ha
- Eligible blocks (age class >= 40): 198987
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.30 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 17.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
