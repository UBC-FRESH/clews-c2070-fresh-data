# WS4 tiled 30-m dataset — H3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H3|BC|S11` (parent `H3|BC`)
- Tile / row / col: `H3` / 1 / 1
- Province: `BC`
- Centroid: 50.658930, -125.080103
- Allocated harvest: 80079.569430 m3
- Productive subcell area: 121520.149298 ha
- Committed geometry area: 218157.094085 ha
- Clipped inventory geometry: 218157.094085 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1675514
- Blocks: 935383
- Forest area: 150796.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87745
- Scheduled area: 12874.68 ha
- Eligible blocks (age class >= 40): 877447
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.43 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 25.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
