# WS4 tiled 30-m dataset — U7|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `U7|NT|S31` (parent `U7|NT`)
- Tile / row / col: `U7` / 3 / 1
- Province: `NT`
- Centroid: 69.438123, -135.497880
- Allocated harvest: 0.470395 m3
- Productive subcell area: 402.145998 ha
- Committed geometry area: 8026.494308 ha
- Clipped inventory geometry: 8026.494308 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 749
- Blocks: 647
- Forest area: 67.41 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 108
- Scheduled area: 9.90 ha
- Eligible blocks (age class >= 40): 108
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.08 MB
- Schedules: 0.00 MB
- Runs: 0.00 MB
- Total: 0.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
