# WS4 tiled 30-m dataset — H26|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H26|QC|S22` (parent `H26|QC`)
- Tile / row / col: `H26` / 2 / 2
- Province: `QC`
- Centroid: 53.163947, -72.319961
- Allocated harvest: 19944.756397 m3
- Productive subcell area: 131905.083658 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1642420
- Blocks: 407145
- Forest area: 147817.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 33509
- Scheduled area: 7740.09 ha
- Eligible blocks (age class >= 40): 335084
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.87 MB
- Schedules: 0.39 MB
- Runs: 0.00 MB
- Total: 17.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
