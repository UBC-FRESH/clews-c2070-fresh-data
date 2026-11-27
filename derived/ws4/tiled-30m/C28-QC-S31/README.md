# WS4 tiled 30-m dataset — C28|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C28|QC|S31` (parent `C28|QC`)
- Tile / row / col: `C28` / 3 / 1
- Province: `QC`
- Centroid: 46.465387, -72.459579
- Allocated harvest: 68782.991452 m3
- Productive subcell area: 124704.896799 ha
- Committed geometry area: 233083.383386 ha
- Clipped inventory geometry: 233083.383386 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1393683
- Blocks: 476901
- Forest area: 125431.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38731
- Scheduled area: 10425.69 ha
- Eligible blocks (age class >= 40): 387301
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.20 MB
- Schedules: 0.46 MB
- Runs: 0.00 MB
- Total: 17.66 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
