# WS4 tiled 30-m dataset — B25|ON|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|ON|S33` (parent `B25|ON`)
- Tile / row / col: `B25` / 3 / 3
- Province: `ON`
- Centroid: 46.041962, -77.503164
- Allocated harvest: 19959.237870 m3
- Productive subcell area: 69199.697969 ha
- Committed geometry area: 52152.050221 ha
- Clipped inventory geometry: 52152.050221 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 460850
- Blocks: 160522
- Forest area: 41476.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 15041
- Scheduled area: 3692.16 ha
- Eligible blocks (age class >= 40): 150402
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.33 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 6.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
