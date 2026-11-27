# WS4 tiled 30-m dataset — I24|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I24|QC|S31` (parent `I24|QC`)
- Tile / row / col: `I24` / 3 / 1
- Province: `QC`
- Centroid: 55.896376, -76.494396
- Allocated harvest: 14433.011470 m3
- Productive subcell area: 91785.299744 ha
- Committed geometry area: 214354.909876 ha
- Clipped inventory geometry: 214354.909876 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1225436
- Blocks: 501309
- Forest area: 110289.24 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 35672
- Scheduled area: 8009.91 ha
- Eligible blocks (age class >= 40): 356719
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.82 MB
- Schedules: 0.42 MB
- Runs: 0.00 MB
- Total: 16.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
