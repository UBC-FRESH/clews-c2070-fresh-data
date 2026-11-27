# WS4 tiled 30-m dataset — D25|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D25|QC|S32` (parent `D25|QC`)
- Tile / row / col: `D25` / 3 / 2
- Province: `QC`
- Centroid: 48.864425, -76.853892
- Allocated harvest: 70742.284250 m3
- Productive subcell area: 191269.768582 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1738872
- Blocks: 693263
- Forest area: 156498.48 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49341
- Scheduled area: 9290.34 ha
- Eligible blocks (age class >= 40): 493410
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.38 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 22.96 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
