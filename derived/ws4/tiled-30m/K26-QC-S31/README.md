# WS4 tiled 30-m dataset — K26|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K26|QC|S31` (parent `K26|QC`)
- Tile / row / col: `K26` / 3 / 1
- Province: `QC`
- Centroid: 57.596666, -70.130909
- Allocated harvest: 21934.268040 m3
- Productive subcell area: 125636.071965 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1303642
- Blocks: 728675
- Forest area: 117327.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59420
- Scheduled area: 9010.08 ha
- Eligible blocks (age class >= 40): 594198
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.56 MB
- Schedules: 0.70 MB
- Runs: 0.00 MB
- Total: 20.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
