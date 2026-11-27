# WS4 tiled 30-m dataset — H31|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S32` (parent `H31|QC`)
- Tile / row / col: `H31` / 3 / 2
- Province: `QC`
- Centroid: 50.681490, -62.020586
- Allocated harvest: 55251.381889 m3
- Productive subcell area: 179522.515524 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2186579
- Blocks: 565221
- Forest area: 196792.11 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52780
- Scheduled area: 18470.88 ha
- Eligible blocks (age class >= 40): 527794
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.79 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 24.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
