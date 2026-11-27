# WS4 tiled 30-m dataset — H29|QC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|QC|S23` (parent `H29|QC`)
- Tile / row / col: `H29` / 2 / 3
- Province: `QC`
- Centroid: 51.349760, -65.524368
- Allocated harvest: 52017.929550 m3
- Productive subcell area: 182295.005519 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1749595
- Blocks: 536724
- Forest area: 157463.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46256
- Scheduled area: 12703.86 ha
- Eligible blocks (age class >= 40): 462556
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.08 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 20.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
