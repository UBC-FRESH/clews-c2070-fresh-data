# WS4 tiled 30-m dataset — H23|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S21` (parent `H23|QC`)
- Tile / row / col: `H23` / 2 / 1
- Province: `QC`
- Centroid: 54.550994, -79.434928
- Allocated harvest: 6609.626681 m3
- Productive subcell area: 35932.089667 ha
- Committed geometry area: 69141.079026 ha
- Clipped inventory geometry: 69141.079026 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 201566
- Blocks: 81929
- Forest area: 18140.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5942
- Scheduled area: 1372.86 ha
- Eligible blocks (age class >= 40): 59414
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.17 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 3.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
