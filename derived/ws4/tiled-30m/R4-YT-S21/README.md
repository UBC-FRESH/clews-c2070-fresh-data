# WS4 tiled 30-m dataset — R4|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R4|YT|S21` (parent `R4|YT`)
- Tile / row / col: `R4` / 2 / 1
- Province: `YT`
- Centroid: 63.453430, -136.972970
- Allocated harvest: 337.589146 m3
- Productive subcell area: 176424.897866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2280364
- Blocks: 660701
- Forest area: 205232.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 58743
- Scheduled area: 15899.13 ha
- Eligible blocks (age class >= 40): 587422
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.21 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 25.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
