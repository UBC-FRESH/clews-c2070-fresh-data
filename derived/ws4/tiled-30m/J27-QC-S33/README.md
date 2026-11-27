# WS4 tiled 30-m dataset — J27|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J27|QC|S33` (parent `J27|QC`)
- Tile / row / col: `J27` / 3 / 3
- Province: `QC`
- Centroid: 55.412547, -67.327439
- Allocated harvest: 17915.927235 m3
- Productive subcell area: 147541.478934 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1788526
- Blocks: 994671
- Forest area: 160967.34 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 92635
- Scheduled area: 15085.08 ha
- Eligible blocks (age class >= 40): 926345
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.13 MB
- Schedules: 1.10 MB
- Runs: 0.00 MB
- Total: 27.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
