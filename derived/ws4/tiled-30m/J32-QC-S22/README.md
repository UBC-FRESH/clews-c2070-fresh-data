# WS4 tiled 30-m dataset — J32|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J32|QC|S22` (parent `J32|QC`)
- Tile / row / col: `J32` / 2 / 2
- Province: `QC`
- Centroid: 51.847933, -58.286821
- Allocated harvest: 26238.404099 m3
- Productive subcell area: 129931.929888 ha
- Committed geometry area: 182924.917867 ha
- Clipped inventory geometry: 182924.917867 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1821371
- Blocks: 474882
- Forest area: 163923.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45761
- Scheduled area: 14802.21 ha
- Eligible blocks (age class >= 40): 457608
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.00 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 20.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
