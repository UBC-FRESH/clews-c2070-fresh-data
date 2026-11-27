# WS4 tiled 30-m dataset — J24|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J24|QC|S13` (parent `J24|QC`)
- Tile / row / col: `J24` / 1 / 3
- Province: `QC`
- Centroid: 56.079623, -74.733249
- Allocated harvest: 10709.596663 m3
- Productive subcell area: 64489.195964 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1092614
- Blocks: 507093
- Forest area: 98335.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37900
- Scheduled area: 7586.73 ha
- Eligible blocks (age class >= 40): 378991
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.67 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 15.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
