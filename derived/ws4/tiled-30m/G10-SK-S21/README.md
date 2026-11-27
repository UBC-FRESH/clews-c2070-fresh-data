# WS4 tiled 30-m dataset — G10|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G10|SK|S21` (parent `G10|SK`)
- Tile / row / col: `G10` / 2 / 1
- Province: `SK`
- Centroid: 53.140298, -109.853759
- Allocated harvest: 8424.284843 m3
- Productive subcell area: 35034.979344 ha
- Committed geometry area: 100064.966485 ha
- Clipped inventory geometry: 100064.966485 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 121509
- Blocks: 53492
- Forest area: 10935.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2480
- Scheduled area: 590.58 ha
- Eligible blocks (age class >= 40): 24799
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.06 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 2.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
