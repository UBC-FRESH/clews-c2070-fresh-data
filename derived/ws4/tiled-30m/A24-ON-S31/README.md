# WS4 tiled 30-m dataset — A24|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `A24|ON|S31` (parent `A24|ON`)
- Tile / row / col: `A24` / 3 / 1
- Province: `ON`
- Centroid: 45.554489, -80.509504
- Allocated harvest: 64.954895 m3
- Productive subcell area: 249.541232 ha
- Committed geometry area: 520.095221 ha
- Clipped inventory geometry: 520.095221 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 4752
- Blocks: 2940
- Forest area: 427.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2752
- Scheduled area: 407.61 ha
- Eligible blocks (age class >= 40): 2752
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.16 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 0.19 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
