# WS4 tiled 30-m dataset — B27|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B27|QC|S32` (parent `B27|QC`)
- Tile / row / col: `B27` / 3 / 2
- Province: `QC`
- Centroid: 45.651341, -74.217615
- Allocated harvest: 26098.946807 m3
- Productive subcell area: 40269.243260 ha
- Committed geometry area: 185282.041670 ha
- Clipped inventory geometry: 185282.041670 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 918205
- Blocks: 289870
- Forest area: 82638.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 21919
- Scheduled area: 7114.59 ha
- Eligible blocks (age class >= 40): 219189
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.89 MB
- Schedules: 0.25 MB
- Runs: 0.00 MB
- Total: 11.14 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
