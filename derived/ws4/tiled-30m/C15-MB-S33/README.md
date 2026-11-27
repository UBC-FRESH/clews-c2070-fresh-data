# WS4 tiled 30-m dataset — C15|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C15|MB|S33` (parent `C15|MB`)
- Tile / row / col: `C15` / 3 / 3
- Province: `MB`
- Centroid: 49.210263, -96.865169
- Allocated harvest: 1587.736033 m3
- Productive subcell area: 37707.257559 ha
- Committed geometry area: 232808.669977 ha
- Clipped inventory geometry: 232808.669977 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 736198
- Blocks: 193418
- Forest area: 66257.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11644
- Scheduled area: 4678.65 ha
- Eligible blocks (age class >= 40): 116431
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.34 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 8.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
