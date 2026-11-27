# WS4 tiled 30-m dataset — D31|NB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D31|NB|S31` (parent `D31|NB`)
- Tile / row / col: `D31` / 3 / 1
- Province: `NB`
- Centroid: 46.124355, -66.380137
- Allocated harvest: 196075.443660 m3
- Productive subcell area: 218596.365827 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2556298
- Blocks: 916143
- Forest area: 230066.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75438
- Scheduled area: 14707.44 ha
- Eligible blocks (age class >= 40): 754380
- Simulated years: 20
- Harvested volume: 2377405.789 m3
- Treated/managed area: 14707.440 ha

## Storage

- Dataset: 30.91 MB
- Schedules: 0.90 MB
- Runs: 16.22 MB
- Total: 48.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
