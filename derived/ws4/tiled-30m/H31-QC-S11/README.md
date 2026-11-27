# WS4 tiled 30-m dataset — H31|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S11` (parent `H31|QC`)
- Tile / row / col: `H31` / 1 / 1
- Province: `QC`
- Centroid: 50.294042, -63.365867
- Allocated harvest: 10344.241138 m3
- Productive subcell area: 33610.456910 ha
- Committed geometry area: 46805.350310 ha
- Clipped inventory geometry: 46805.350310 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 211150
- Blocks: 113710
- Forest area: 19003.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 9779
- Scheduled area: 1735.11 ha
- Eligible blocks (age class >= 40): 97786
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 3.88 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 3.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
