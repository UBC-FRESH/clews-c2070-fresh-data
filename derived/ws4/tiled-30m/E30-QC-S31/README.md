# WS4 tiled 30-m dataset — E30|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E30|QC|S31` (parent `E30|QC`)
- Tile / row / col: `E30` / 3 / 1
- Province: `QC`
- Centroid: 48.013278, -67.291574
- Allocated harvest: 69613.477753 m3
- Productive subcell area: 114855.630664 ha
- Committed geometry area: 124460.024930 ha
- Clipped inventory geometry: 124460.024930 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1302991
- Blocks: 410337
- Forest area: 117269.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36664
- Scheduled area: 10228.14 ha
- Eligible blocks (age class >= 40): 366635
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.74 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 16.17 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
