# WS4 tiled 30-m dataset — Q3|YT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q3|YT|S21` (parent `Q3|YT`)
- Tile / row / col: `Q3` / 2 / 1
- Province: `YT`
- Centroid: 61.505587, -137.486839
- Allocated harvest: 255.809910 m3
- Productive subcell area: 171969.252036 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1106792
- Blocks: 523634
- Forest area: 99611.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41135
- Scheduled area: 7664.22 ha
- Eligible blocks (age class >= 40): 411349
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.42 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 15.91 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
