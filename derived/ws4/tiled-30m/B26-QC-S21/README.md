# WS4 tiled 30-m dataset — B26|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|QC|S21` (parent `B26|QC`)
- Tile / row / col: `B26` / 2 / 1
- Province: `QC`
- Centroid: 45.728080, -76.715797
- Allocated harvest: 24081.816193 m3
- Productive subcell area: 39934.780839 ha
- Committed geometry area: 49605.254514 ha
- Clipped inventory geometry: 49605.254514 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 319997
- Blocks: 116647
- Forest area: 28799.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 10107
- Scheduled area: 2917.35 ha
- Eligible blocks (age class >= 40): 101070
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.70 MB
- Schedules: 0.11 MB
- Runs: 0.00 MB
- Total: 4.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
