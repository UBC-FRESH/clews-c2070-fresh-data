# WS4 tiled 30-m dataset — R3|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R3|YT|S21` (parent `R3|YT`)
- Tile / row / col: `R3` / 2 / 1
- Province: `YT`
- Centroid: 62.582155, -139.350999
- Allocated harvest: 467.006597 m3
- Productive subcell area: 188247.032413 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2202299
- Blocks: 792017
- Forest area: 198206.91 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 70473
- Scheduled area: 15497.55 ha
- Eligible blocks (age class >= 40): 704727
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.77 MB
- Schedules: 0.84 MB
- Runs: 0.00 MB
- Total: 27.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
