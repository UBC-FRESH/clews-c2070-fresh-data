# WS4 tiled 30-m dataset — M9|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|NT|S13` (parent `M9|NT`)
- Tile / row / col: `M9` / 1 / 3
- Province: `NT`
- Centroid: 60.529546, -114.737255
- Allocated harvest: 138.439066 m3
- Productive subcell area: 109450.097673 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1923055
- Blocks: 629891
- Forest area: 173074.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46839
- Scheduled area: 11710.89 ha
- Eligible blocks (age class >= 40): 468383
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.94 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 22.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
