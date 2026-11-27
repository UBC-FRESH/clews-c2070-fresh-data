# WS4 tiled 30-m dataset — C29|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C29|QC|S31` (parent `C29|QC`)
- Tile / row / col: `C29` / 3 / 1
- Province: `QC`
- Centroid: 45.982564, -70.660329
- Allocated harvest: 143770.965216 m3
- Productive subcell area: 250458.113008 ha
- Committed geometry area: 247747.043691 ha
- Clipped inventory geometry: 247747.043691 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2170886
- Blocks: 707979
- Forest area: 195379.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59987
- Scheduled area: 16121.88 ha
- Eligible blocks (age class >= 40): 599862
- Simulated years: 20
- Harvested volume: 2914715.916 m3
- Treated/managed area: 16121.880 ha

## Storage

- Dataset: 25.36 MB
- Schedules: 0.71 MB
- Runs: 17.52 MB
- Total: 43.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
