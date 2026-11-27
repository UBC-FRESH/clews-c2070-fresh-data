# WS4 tiled 30-m dataset — H12|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H12|SK|S22` (parent `H12|SK`)
- Tile / row / col: `H12` / 2 / 2
- Province: `SK`
- Centroid: 55.107480, -105.202281
- Allocated harvest: 38175.937083 m3
- Productive subcell area: 196432.148373 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 880658
- Blocks: 384033
- Forest area: 79259.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35459
- Scheduled area: 6744.42 ha
- Eligible blocks (age class >= 40): 354587
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.95 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 12.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
