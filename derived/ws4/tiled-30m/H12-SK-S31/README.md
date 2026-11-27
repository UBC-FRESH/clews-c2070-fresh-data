# WS4 tiled 30-m dataset — H12|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H12|SK|S31` (parent `H12|SK`)
- Tile / row / col: `H12` / 3 / 1
- Province: `SK`
- Centroid: 55.482725, -106.127894
- Allocated harvest: 38175.937083 m3
- Productive subcell area: 196432.148373 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1382725
- Blocks: 467486
- Forest area: 124445.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38437
- Scheduled area: 6312.69 ha
- Eligible blocks (age class >= 40): 384361
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.24 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 16.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
