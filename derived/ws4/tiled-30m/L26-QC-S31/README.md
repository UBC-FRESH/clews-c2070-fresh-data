# WS4 tiled 30-m dataset — L26|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S31` (parent `L26|QC`)
- Tile / row / col: `L26` / 3 / 1
- Province: `QC`
- Centroid: 58.815502, -69.130358
- Allocated harvest: 10216.938061 m3
- Productive subcell area: 58483.663981 ha
- Committed geometry area: 157248.190466 ha
- Clipped inventory geometry: 157248.190466 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 5752
- Blocks: 5192
- Forest area: 517.68 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1027
- Scheduled area: 96.75 ha
- Eligible blocks (age class >= 40): 1027
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.20 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.21 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
