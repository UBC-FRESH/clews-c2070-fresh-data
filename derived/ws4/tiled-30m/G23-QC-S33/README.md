# WS4 tiled 30-m dataset — G23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G23|QC|S33` (parent `G23|QC`)
- Tile / row / col: `G23` / 3 / 3
- Province: `QC`
- Centroid: 53.402195, -78.568113
- Allocated harvest: 26537.034697 m3
- Productive subcell area: 145927.852750 ha
- Committed geometry area: 241432.337985 ha
- Clipped inventory geometry: 241432.337985 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1860222
- Blocks: 838677
- Forest area: 167419.98 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73611
- Scheduled area: 14005.26 ha
- Eligible blocks (age class >= 40): 736101
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.49 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 25.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
