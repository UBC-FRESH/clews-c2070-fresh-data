# WS4 tiled 30-m dataset — L7|AB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L7|AB|S33` (parent `L7|AB`)
- Tile / row / col: `L7` / 3 / 3
- Province: `AB`
- Centroid: 59.144820, -119.568365
- Allocated harvest: 112142.683462 m3
- Productive subcell area: 198618.103656 ha
- Committed geometry area: 235109.675172 ha
- Clipped inventory geometry: 235109.675172 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1935730
- Blocks: 871674
- Forest area: 174215.70 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 74940
- Scheduled area: 13607.55 ha
- Eligible blocks (age class >= 40): 749395
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.76 MB
- Schedules: 0.89 MB
- Runs: 0.00 MB
- Total: 26.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
