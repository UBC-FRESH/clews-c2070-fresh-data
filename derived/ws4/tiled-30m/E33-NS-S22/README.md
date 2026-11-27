# WS4 tiled 30-m dataset — E33|NS|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|NS|S22` (parent `E33|NS`)
- Tile / row / col: `E33` / 2 / 2
- Province: `NS`
- Centroid: 45.452396, -61.861250
- Allocated harvest: 95908.080787 m3
- Productive subcell area: 199548.771677 ha
- Committed geometry area: 240696.805473 ha
- Clipped inventory geometry: 240696.805473 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2218785
- Blocks: 794624
- Forest area: 199690.65 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62910
- Scheduled area: 12972.06 ha
- Eligible blocks (age class >= 40): 629097
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.94 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 27.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
