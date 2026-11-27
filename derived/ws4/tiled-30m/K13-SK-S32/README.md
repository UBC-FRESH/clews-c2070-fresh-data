# WS4 tiled 30-m dataset — K13|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S32` (parent `K13|SK`)
- Tile / row / col: `K13` / 3 / 2
- Province: `SK`
- Centroid: 59.816763, -103.950649
- Allocated harvest: 10746.326377 m3
- Productive subcell area: 113553.188039 ha
- Committed geometry area: 200420.812827 ha
- Clipped inventory geometry: 200420.812827 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1297048
- Blocks: 355123
- Forest area: 116734.32 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28544
- Scheduled area: 6457.32 ha
- Eligible blocks (age class >= 40): 285431
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.79 MB
- Schedules: 0.33 MB
- Runs: 0.00 MB
- Total: 14.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
