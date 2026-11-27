# WS4 tiled 30-m dataset — C16|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C16|MB|S31` (parent `C16|MB`)
- Tile / row / col: `C16` / 3 / 1
- Province: `MB`
- Centroid: 49.215548, -96.179067
- Allocated harvest: 9730.827333 m3
- Productive subcell area: 182006.932478 ha
- Committed geometry area: 238902.287294 ha
- Clipped inventory geometry: 238902.287294 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1686082
- Blocks: 564657
- Forest area: 151747.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46616
- Scheduled area: 12538.62 ha
- Eligible blocks (age class >= 40): 466156
- Simulated years: 20
- Harvested volume: 1608744.812 m3
- Treated/managed area: 12538.620 ha

## Storage

- Dataset: 20.28 MB
- Schedules: 0.55 MB
- Runs: 13.60 MB
- Total: 34.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
