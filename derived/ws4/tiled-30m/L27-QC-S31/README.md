# WS4 tiled 30-m dataset — L27|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L27|QC|S31` (parent `L27|QC`)
- Tile / row / col: `L27` / 3 / 1
- Province: `QC`
- Centroid: 58.277333, -66.686625
- Allocated harvest: 13542.888638 m3
- Productive subcell area: 83439.333631 ha
- Committed geometry area: 226925.688177 ha
- Clipped inventory geometry: 226925.688177 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 727442
- Blocks: 370778
- Forest area: 65469.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25649
- Scheduled area: 3915.81 ha
- Eligible blocks (age class >= 40): 256483
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 10.43 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 10.73 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
