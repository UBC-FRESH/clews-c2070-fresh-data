# WS4 tiled 30-m dataset — E25|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E25|QC|S31` (parent `E25|QC`)
- Tile / row / col: `E25` / 3 / 1
- Province: `QC`
- Centroid: 50.288161, -76.935159
- Allocated harvest: 47773.618433 m3
- Productive subcell area: 170907.680670 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2174364
- Blocks: 772881
- Forest area: 195692.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62450
- Scheduled area: 13742.82 ha
- Eligible blocks (age class >= 40): 624494
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.68 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 27.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
