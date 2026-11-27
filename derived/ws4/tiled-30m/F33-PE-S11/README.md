# WS4 tiled 30-m dataset — F33|PE|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F33|PE|S11` (parent `F33|PE`)
- Tile / row / col: `F33` / 1 / 1
- Province: `PE`
- Centroid: 46.421880, -62.104682
- Allocated harvest: 4644.057445 m3
- Productive subcell area: 6127.059594 ha
- Committed geometry area: 12331.089939 ha
- Clipped inventory geometry: 12331.089939 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 77427
- Blocks: 38983
- Forest area: 6968.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3367
- Scheduled area: 588.87 ha
- Eligible blocks (age class >= 40): 33668
- Simulated years: 20
- Harvested volume: 51901.411 m3
- Treated/managed area: 588.870 ha

## Storage

- Dataset: 1.45 MB
- Schedules: 0.04 MB
- Runs: 0.65 MB
- Total: 2.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
