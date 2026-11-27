# WS4 tiled 30-m dataset — O3|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O3|YT|S33` (parent `O3|YT`)
- Tile / row / col: `O3` / 3 / 3
- Province: `YT`
- Centroid: 60.212744, -133.150220
- Allocated harvest: 578.457677 m3
- Productive subcell area: 191423.847660 ha
- Committed geometry area: 228474.167930 ha
- Clipped inventory geometry: 228474.167930 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2154768
- Blocks: 928237
- Forest area: 193929.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87437
- Scheduled area: 17218.08 ha
- Eligible blocks (age class >= 40): 874365
- Simulated years: 20
- Harvested volume: 2528972.819 m3
- Treated/managed area: 17218.080 ha

## Storage

- Dataset: 28.06 MB
- Schedules: 1.04 MB
- Runs: 18.95 MB
- Total: 48.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
