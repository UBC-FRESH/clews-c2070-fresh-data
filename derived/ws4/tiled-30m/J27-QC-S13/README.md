# WS4 tiled 30-m dataset — J27|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|QC|S13` (parent `J27|QC`)
- Tile / row / col: `J27` / 1 / 3
- Province: `QC`
- Centroid: 54.582635, -67.995826
- Allocated harvest: 17625.711777 m3
- Productive subcell area: 145151.492789 ha
- Committed geometry area: 245950.314850 ha
- Clipped inventory geometry: 245950.314850 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1659614
- Blocks: 702612
- Forest area: 149365.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63506
- Scheduled area: 14700.06 ha
- Eligible blocks (age class >= 40): 635056
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.75 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 22.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
