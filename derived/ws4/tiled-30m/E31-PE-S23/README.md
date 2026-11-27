# WS4 tiled 30-m dataset — E31|PE|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E31|PE|S23` (parent `E31|PE`)
- Tile / row / col: `E31` / 2 / 3
- Province: `PE`
- Centroid: 46.644813, -64.353420
- Allocated harvest: 3227.792269 m3
- Productive subcell area: 2455.775807 ha
- Committed geometry area: 4275.939324 ha
- Clipped inventory geometry: 4275.939324 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 25500
- Blocks: 10450
- Forest area: 2295.00 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 792
- Scheduled area: 164.16 ha
- Eligible blocks (age class >= 40): 7916
- Simulated years: 20
- Harvested volume: 26245.398 m3
- Treated/managed area: 164.160 ha

## Storage

- Dataset: 0.48 MB
- Schedules: 0.01 MB
- Runs: 0.18 MB
- Total: 0.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
