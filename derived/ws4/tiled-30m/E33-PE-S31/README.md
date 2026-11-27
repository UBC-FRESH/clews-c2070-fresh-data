# WS4 tiled 30-m dataset — E33|PE|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E33|PE|S31` (parent `E33|PE`)
- Tile / row / col: `E33` / 3 / 1
- Province: `PE`
- Centroid: 45.999512, -62.491910
- Allocated harvest: 1177.210470 m3
- Productive subcell area: 1070.131613 ha
- Committed geometry area: 2153.706678 ha
- Clipped inventory geometry: 2153.706678 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 9582
- Blocks: 4633
- Forest area: 862.38 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3677
- Scheduled area: 653.22 ha
- Eligible blocks (age class >= 40): 3677
- Simulated years: 20
- Harvested volume: 82906.064 m3
- Treated/managed area: 653.220 ha

## Storage

- Dataset: 0.23 MB
- Schedules: 0.04 MB
- Runs: 0.72 MB
- Total: 0.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
