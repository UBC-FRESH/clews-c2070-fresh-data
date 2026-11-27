# WS4 tiled 30-m dataset — B25|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B25|QC|S31` (parent `B25|QC`)
- Tile / row / col: `B25` / 3 / 1
- Province: `QC`
- Centroid: 46.469014, -78.517453
- Allocated harvest: 78671.329325 m3
- Productive subcell area: 140445.278842 ha
- Committed geometry area: 165136.413566 ha
- Clipped inventory geometry: 165136.413566 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1645584
- Blocks: 496983
- Forest area: 148102.56 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48282
- Scheduled area: 14092.29 ha
- Eligible blocks (age class >= 40): 482819
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.37 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 19.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
