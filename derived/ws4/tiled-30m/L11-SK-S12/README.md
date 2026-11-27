# WS4 tiled 30-m dataset — L11|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|SK|S12` (parent `L11|SK`)
- Tile / row / col: `L11` / 1 / 2
- Province: `SK`
- Centroid: 59.787121, -109.529247
- Allocated harvest: 16412.121461 m3
- Productive subcell area: 142165.438521 ha
- Committed geometry area: 226549.058596 ha
- Clipped inventory geometry: 226549.058596 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1736895
- Blocks: 281636
- Forest area: 156320.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14635
- Scheduled area: 3609.27 ha
- Eligible blocks (age class >= 40): 146348
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.26 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 15.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
