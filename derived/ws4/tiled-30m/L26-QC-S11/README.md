# WS4 tiled 30-m dataset — L26|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L26|QC|S11` (parent `L26|QC`)
- Tile / row / col: `L26` / 1 / 1
- Province: `QC`
- Centroid: 58.021818, -69.800151
- Allocated harvest: 16243.331689 m3
- Productive subcell area: 92979.868016 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 384313
- Blocks: 234578
- Forest area: 34588.17 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14378
- Scheduled area: 1858.59 ha
- Eligible blocks (age class >= 40): 143780
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.55 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 6.72 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
