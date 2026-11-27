# WS4 tiled 30-m dataset — E32|PE|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E32|PE|S33` (parent `E32|PE`)
- Tile / row / col: `E32` / 3 / 3
- Province: `PE`
- Centroid: 46.264850, -62.670813
- Allocated harvest: 92889.831456 m3
- Productive subcell area: 85960.296483 ha
- Committed geometry area: 190502.662764 ha
- Clipped inventory geometry: 190502.662764 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1090053
- Blocks: 463089
- Forest area: 98104.77 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36390
- Scheduled area: 7083.90 ha
- Eligible blocks (age class >= 40): 363895
- Simulated years: 20
- Harvested volume: 902300.236 m3
- Treated/managed area: 7083.900 ha

## Storage

- Dataset: 14.46 MB
- Schedules: 0.43 MB
- Runs: 7.80 MB
- Total: 22.68 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
