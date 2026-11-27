# WS4 tiled 30-m dataset — D24|ON|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|ON|S21` (parent `D24|ON`)
- Tile / row / col: `D24` / 2 / 1
- Province: `ON`
- Centroid: 48.900253, -79.758260
- Allocated harvest: 33432.320456 m3
- Productive subcell area: 160910.782816 ha
- Committed geometry area: 179874.644807 ha
- Clipped inventory geometry: 179874.644807 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1328325
- Blocks: 477730
- Forest area: 119549.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 42569
- Scheduled area: 9371.88 ha
- Eligible blocks (age class >= 40): 425681
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.47 MB
- Schedules: 0.50 MB
- Runs: 0.00 MB
- Total: 16.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
