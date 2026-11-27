# WS4 tiled 30-m dataset — G14|MB|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G14|MB|S21` (parent `G14|MB`)
- Tile / row / col: `G14` / 2 / 1
- Province: `MB`
- Centroid: 54.036403, -100.997629
- Allocated harvest: 5805.608277 m3
- Productive subcell area: 146461.461203 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1247569
- Blocks: 462628
- Forest area: 112281.21 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41278
- Scheduled area: 9586.98 ha
- Eligible blocks (age class >= 40): 412773
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.85 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 16.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
