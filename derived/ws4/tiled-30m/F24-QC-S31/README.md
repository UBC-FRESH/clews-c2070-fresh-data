# WS4 tiled 30-m dataset — F24|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F24|QC|S31` (parent `F24|QC`)
- Tile / row / col: `F24` / 3 / 1
- Province: `QC`
- Centroid: 51.944238, -78.402793
- Allocated harvest: 27616.554883 m3
- Productive subcell area: 135437.470659 ha
- Committed geometry area: 221893.419326 ha
- Clipped inventory geometry: 221893.419326 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1659138
- Blocks: 558204
- Forest area: 149322.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 50124
- Scheduled area: 11174.76 ha
- Eligible blocks (age class >= 40): 501233
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.56 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 20.15 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
