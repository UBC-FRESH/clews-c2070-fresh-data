# WS4 tiled 30-m dataset — H18|MB|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H18|MB|S22` (parent `H18|MB`)
- Tile / row / col: `H18` / 2 / 2
- Province: `MB`
- Centroid: 55.655363, -91.013678
- Allocated harvest: 313.883449 m3
- Productive subcell area: 15565.883179 ha
- Committed geometry area: 25376.577893 ha
- Clipped inventory geometry: 25376.577893 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 211960
- Blocks: 78428
- Forest area: 19076.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 7194
- Scheduled area: 1642.77 ha
- Eligible blocks (age class >= 40): 71934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.16 MB
- Schedules: 0.08 MB
- Runs: 0.00 MB
- Total: 3.24 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
