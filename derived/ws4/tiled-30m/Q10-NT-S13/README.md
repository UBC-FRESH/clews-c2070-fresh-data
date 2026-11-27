# WS4 tiled 30-m dataset — Q10|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q10|NT|S13` (parent `Q10|NT`)
- Tile / row / col: `Q10` / 1 / 3
- Province: `NT`
- Centroid: 66.219546, -115.684889
- Allocated harvest: 32.934790 m3
- Productive subcell area: 76567.382158 ha
- Committed geometry area: 233049.195200 ha
- Clipped inventory geometry: 233049.195200 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 637833
- Blocks: 382707
- Forest area: 57404.97 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23796
- Scheduled area: 3332.43 ha
- Eligible blocks (age class >= 40): 237951
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.03 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 10.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
