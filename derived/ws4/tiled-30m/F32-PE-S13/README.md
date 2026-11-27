# WS4 tiled 30-m dataset — F32|PE|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F32|PE|S13` (parent `F32|PE`)
- Tile / row / col: `F32` / 1 / 3
- Province: `PE`
- Centroid: 46.439551, -62.269805
- Allocated harvest: 7476.731700 m3
- Productive subcell area: 8416.730943 ha
- Committed geometry area: 16939.196470 ha
- Clipped inventory geometry: 16939.196470 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 145228
- Blocks: 61728
- Forest area: 13070.52 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5356
- Scheduled area: 1031.58 ha
- Eligible blocks (age class >= 40): 53555
- Simulated years: 20
- Harvested volume: 107613.600 m3
- Treated/managed area: 1031.580 ha

## Storage

- Dataset: 2.44 MB
- Schedules: 0.06 MB
- Runs: 1.13 MB
- Total: 3.63 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
