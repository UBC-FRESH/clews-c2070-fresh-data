# WS4 tiled 30-m dataset — H31|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S31` (parent `H31|QC`)
- Tile / row / col: `H31` / 3 / 1
- Province: `QC`
- Centroid: 50.903781, -62.642294
- Allocated harvest: 55251.381889 m3
- Productive subcell area: 179522.515524 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2309398
- Blocks: 519005
- Forest area: 207845.82 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49347
- Scheduled area: 20915.73 ha
- Eligible blocks (age class >= 40): 493465
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.23 MB
- Schedules: 0.58 MB
- Runs: 0.00 MB
- Total: 24.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
