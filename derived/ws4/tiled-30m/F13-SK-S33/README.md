# WS4 tiled 30-m dataset — F13|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|SK|S33` (parent `F13|SK`)
- Tile / row / col: `F13` / 3 / 3
- Province: `SK`
- Centroid: 53.073802, -101.837869
- Allocated harvest: 17389.542939 m3
- Productive subcell area: 70225.555440 ha
- Committed geometry area: 97892.824050 ha
- Clipped inventory geometry: 97892.824050 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 898825
- Blocks: 350300
- Forest area: 80894.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33737
- Scheduled area: 7917.48 ha
- Eligible blocks (age class >= 40): 337366
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.70 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 12.09 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
