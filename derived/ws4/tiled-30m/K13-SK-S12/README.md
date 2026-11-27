# WS4 tiled 30-m dataset — K13|SK|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S12` (parent `K13|SK`)
- Tile / row / col: `K13` / 1 / 2
- Province: `SK`
- Centroid: 58.948647, -103.699531
- Allocated harvest: 13404.703615 m3
- Productive subcell area: 141643.458128 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1591852
- Blocks: 342026
- Forest area: 143266.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22481
- Scheduled area: 5402.52 ha
- Eligible blocks (age class >= 40): 224809
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.60 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 15.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
