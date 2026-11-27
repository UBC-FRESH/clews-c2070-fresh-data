# WS4 tiled 30-m dataset — E31|NB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|NB|S13` (parent `E31|NB`)
- Tile / row / col: `E31` / 1 / 3
- Province: `NB`
- Centroid: 46.127205, -64.952830
- Allocated harvest: 179666.627959 m3
- Productive subcell area: 224372.467176 ha
- Committed geometry area: 247544.437646 ha
- Clipped inventory geometry: 247544.437646 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2279498
- Blocks: 827359
- Forest area: 205154.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65463
- Scheduled area: 13428.45 ha
- Eligible blocks (age class >= 40): 654630
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.76 MB
- Schedules: 0.78 MB
- Runs: 0.00 MB
- Total: 28.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
