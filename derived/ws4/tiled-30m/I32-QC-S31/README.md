# WS4 tiled 30-m dataset — I32|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S31` (parent `I32|QC`)
- Tile / row / col: `I32` / 3 / 1
- Province: `QC`
- Centroid: 51.385725, -59.684548
- Allocated harvest: 41055.309093 m3
- Productive subcell area: 176040.436917 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2323203
- Blocks: 645093
- Forest area: 209088.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62358
- Scheduled area: 20530.98 ha
- Eligible blocks (age class >= 40): 623580
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.91 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 26.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
