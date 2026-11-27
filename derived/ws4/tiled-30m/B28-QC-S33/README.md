# WS4 tiled 30-m dataset — B28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B28|QC|S33` (parent `B28|QC`)
- Tile / row / col: `B28` / 3 / 3
- Province: `QC`
- Centroid: 45.071306, -71.932615
- Allocated harvest: 20236.507846 m3
- Productive subcell area: 32471.726693 ha
- Committed geometry area: 62674.639892 ha
- Clipped inventory geometry: 62674.639892 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 507902
- Blocks: 166779
- Forest area: 45711.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 13282
- Scheduled area: 3715.29 ha
- Eligible blocks (age class >= 40): 132819
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.70 MB
- Schedules: 0.15 MB
- Runs: 0.00 MB
- Total: 6.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
