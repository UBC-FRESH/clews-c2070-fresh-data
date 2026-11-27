# WS4 tiled 30-m dataset — F4|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F4|BC|S21` (parent `F4|BC`)
- Tile / row / col: `F4` / 2 / 1
- Province: `BC`
- Centroid: 49.216148, -121.667237
- Allocated harvest: 176337.257835 m3
- Productive subcell area: 175380.614262 ha
- Committed geometry area: 234575.836563 ha
- Clipped inventory geometry: 234575.836563 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2086408
- Blocks: 1053615
- Forest area: 187776.72 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 99064
- Scheduled area: 15956.46 ha
- Eligible blocks (age class >= 40): 990633
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.90 MB
- Schedules: 1.18 MB
- Runs: 0.00 MB
- Total: 30.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
