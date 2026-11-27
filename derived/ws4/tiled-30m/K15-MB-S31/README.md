# WS4 tiled 30-m dataset — K15|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K15|MB|S31` (parent `K15|MB`)
- Tile / row / col: `K15` / 3 / 1
- Province: `MB`
- Centroid: 59.936907, -99.363339
- Allocated harvest: 494.085422 m3
- Productive subcell area: 28736.150311 ha
- Committed geometry area: 69047.814021 ha
- Clipped inventory geometry: 69047.814021 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 298768
- Blocks: 131742
- Forest area: 26889.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9904
- Scheduled area: 1974.87 ha
- Eligible blocks (age class >= 40): 99034
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.76 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.87 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
