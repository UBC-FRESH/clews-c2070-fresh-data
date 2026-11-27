# WS4 tiled 30-m dataset — K11|AB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|AB|S21` (parent `K11|AB`)
- Tile / row / col: `K11` / 2 / 1
- Province: `AB`
- Centroid: 58.795162, -110.216393
- Allocated harvest: 14264.419132 m3
- Productive subcell area: 64830.856245 ha
- Committed geometry area: 122659.356234 ha
- Clipped inventory geometry: 122659.356234 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 674680
- Blocks: 202211
- Forest area: 60721.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17403
- Scheduled area: 4213.98 ha
- Eligible blocks (age class >= 40): 174026
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.91 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 8.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
