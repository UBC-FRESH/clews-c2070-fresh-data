# WS4 tiled 30-m dataset — G2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S32` (parent `G2|BC`)
- Tile / row / col: `G2` / 3 / 2
- Province: `BC`
- Centroid: 49.836521, -125.994053
- Allocated harvest: 228408.176800 m3
- Productive subcell area: 224737.998031 ha
- Committed geometry area: 247332.369040 ha
- Clipped inventory geometry: 247332.369040 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2445603
- Blocks: 931483
- Forest area: 220104.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 89847
- Scheduled area: 18121.23 ha
- Eligible blocks (age class >= 40): 898468
- Simulated years: 20
- Harvested volume: 6647969.804 m3
- Treated/managed area: 18121.230 ha

## Storage

- Dataset: 29.84 MB
- Schedules: 1.07 MB
- Runs: 19.87 MB
- Total: 50.77 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
