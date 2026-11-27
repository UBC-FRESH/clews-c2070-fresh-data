# WS4 tiled 30-m dataset — K7|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|BC|S11` (parent `K7|BC`)
- Tile / row / col: `K7` / 1 / 1
- Province: `BC`
- Centroid: 56.752455, -120.038423
- Allocated harvest: 2549.383060 m3
- Productive subcell area: 6364.679932 ha
- Committed geometry area: 6705.156840 ha
- Clipped inventory geometry: 6705.156840 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 71792
- Blocks: 23403
- Forest area: 6461.28 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1600
- Scheduled area: 285.75 ha
- Eligible blocks (age class >= 40): 15992
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.08 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
