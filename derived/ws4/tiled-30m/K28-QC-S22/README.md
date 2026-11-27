# WS4 tiled 30-m dataset — K28|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K28|QC|S22` (parent `K28|QC`)
- Tile / row / col: `K28` / 2 / 2
- Province: `QC`
- Centroid: 55.836852, -65.161788
- Allocated harvest: 15232.710995 m3
- Productive subcell area: 118257.331241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1408687
- Blocks: 778188
- Forest area: 126781.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 67615
- Scheduled area: 10577.07 ha
- Eligible blocks (age class >= 40): 676141
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.72 MB
- Schedules: 0.80 MB
- Runs: 0.00 MB
- Total: 21.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
