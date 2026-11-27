# WS4 tiled 30-m dataset — J32|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S33` (parent `J32|QC`)
- Tile / row / col: `J32` / 3 / 3
- Province: `QC`
- Centroid: 51.900376, -57.350782
- Allocated harvest: 11514.416261 m3
- Productive subcell area: 57019.105304 ha
- Committed geometry area: 80274.457275 ha
- Clipped inventory geometry: 80274.457275 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 610731
- Blocks: 313069
- Forest area: 54965.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 26354
- Scheduled area: 4600.53 ha
- Eligible blocks (age class >= 40): 263535
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.22 MB
- Schedules: 0.31 MB
- Runs: 0.00 MB
- Total: 9.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
