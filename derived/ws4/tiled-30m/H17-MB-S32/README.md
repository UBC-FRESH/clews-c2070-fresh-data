# WS4 tiled 30-m dataset — H17|MB|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H17|MB|S32` (parent `H17|MB`)
- Tile / row / col: `H17` / 3 / 2
- Province: `MB`
- Centroid: 56.019039, -93.130486
- Allocated harvest: 3671.317445 m3
- Productive subcell area: 166044.572865 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1795562
- Blocks: 790670
- Forest area: 161600.58 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 68059
- Scheduled area: 12991.05 ha
- Eligible blocks (age class >= 40): 680581
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.77 MB
- Schedules: 0.81 MB
- Runs: 0.00 MB
- Total: 24.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
