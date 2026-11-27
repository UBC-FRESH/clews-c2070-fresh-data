# WS4 tiled 30-m dataset — J29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J29|QC|S31` (parent `J29|QC`)
- Tile / row / col: `J29` / 3 / 1
- Province: `QC`
- Centroid: 54.796085, -64.595178
- Allocated harvest: 4263.464044 m3
- Productive subcell area: 26512.435919 ha
- Committed geometry area: 54791.528362 ha
- Clipped inventory geometry: 54791.528362 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 290644
- Blocks: 162485
- Forest area: 26157.96 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14419
- Scheduled area: 2443.41 ha
- Eligible blocks (age class >= 40): 144189
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.15 MB
- Schedules: 0.16 MB
- Runs: 0.00 MB
- Total: 5.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
