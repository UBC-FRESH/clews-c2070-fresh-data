# WS4 tiled 30-m dataset — F29|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S22` (parent `F29|QC`)
- Tile / row / col: `F29` / 2 / 2
- Province: `QC`
- Centroid: 49.109857, -68.276421
- Allocated harvest: 15231.505729 m3
- Productive subcell area: 33071.805565 ha
- Committed geometry area: 39393.869566 ha
- Clipped inventory geometry: 39393.869566 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 331307
- Blocks: 137892
- Forest area: 29817.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12739
- Scheduled area: 2875.05 ha
- Eligible blocks (age class >= 40): 127382
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 5.12 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 5.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
