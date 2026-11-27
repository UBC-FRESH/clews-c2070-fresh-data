# WS4 tiled 30-m dataset — C26|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C26|QC|S31` (parent `C26|QC`)
- Tile / row / col: `C26` / 3 / 1
- Province: `QC`
- Centroid: 47.319770, -76.147840
- Allocated harvest: 127938.356993 m3
- Productive subcell area: 207690.437894 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2426666
- Blocks: 797234
- Forest area: 218399.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73539
- Scheduled area: 19127.43 ha
- Eligible blocks (age class >= 40): 735390
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 28.93 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 29.80 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
