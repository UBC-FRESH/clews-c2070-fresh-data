# WS4 tiled 30-m dataset — E32|PE|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S22` (parent `E32|PE`)
- Tile / row / col: `E32` / 2 / 2
- Province: `PE`
- Centroid: 46.260913, -63.459917
- Allocated harvest: 31758.857778 m3
- Productive subcell area: 29389.662870 ha
- Committed geometry area: 65132.500276 ha
- Clipped inventory geometry: 65132.500276 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 232566
- Blocks: 111346
- Forest area: 20930.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7929
- Scheduled area: 1562.22 ha
- Eligible blocks (age class >= 40): 79285
- Simulated years: 20
- Harvested volume: 210119.495 m3
- Treated/managed area: 1562.220 ha

## Storage

- Dataset: 3.96 MB
- Schedules: 0.09 MB
- Runs: 1.72 MB
- Total: 5.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
