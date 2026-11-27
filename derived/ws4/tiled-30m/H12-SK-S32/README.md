# WS4 tiled 30-m dataset — H12|SK|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H12|SK|S32` (parent `H12|SK`)
- Tile / row / col: `H12` / 3 / 2
- Province: `SK`
- Centroid: 55.559678, -105.331450
- Allocated harvest: 38175.937083 m3
- Productive subcell area: 196432.148373 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1218567
- Blocks: 338779
- Forest area: 109671.03 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25176
- Scheduled area: 4519.44 ha
- Eligible blocks (age class >= 40): 251760
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.35 MB
- Schedules: 0.29 MB
- Runs: 0.00 MB
- Total: 13.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
