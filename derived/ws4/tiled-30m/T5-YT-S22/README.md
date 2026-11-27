# WS4 tiled 30-m dataset — T5|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T5|YT|S22` (parent `T5|YT`)
- Tile / row / col: `T5` / 2 / 2
- Province: `YT`
- Centroid: 66.778569, -137.579256
- Allocated harvest: 216.789563 m3
- Productive subcell area: 131519.529150 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1389311
- Blocks: 355293
- Forest area: 125037.99 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20470
- Scheduled area: 4059.09 ha
- Eligible blocks (age class >= 40): 204699
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.37 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 14.61 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
