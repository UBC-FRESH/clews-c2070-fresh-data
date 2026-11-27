# WS4 tiled 30-m dataset — D24|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D24|QC|S11` (parent `D24|QC`)
- Tile / row / col: `D24` / 1 / 1
- Province: `QC`
- Centroid: 48.540585, -79.483542
- Allocated harvest: 3988.481918 m3
- Productive subcell area: 10054.256510 ha
- Committed geometry area: 12245.599407 ha
- Clipped inventory geometry: 12245.599407 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 111193
- Blocks: 37728
- Forest area: 10007.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3346
- Scheduled area: 689.94 ha
- Eligible blocks (age class >= 40): 33451
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.70 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
