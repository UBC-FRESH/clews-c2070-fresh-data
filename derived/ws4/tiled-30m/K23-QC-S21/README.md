# WS4 tiled 30-m dataset — K23|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K23|QC|S21` (parent `K23|QC`)
- Tile / row / col: `K23` / 2 / 1
- Province: `QC`
- Centroid: 58.531438, -77.766328
- Allocated harvest: 970.537593 m3
- Productive subcell area: 7174.446354 ha
- Committed geometry area: 214684.251689 ha
- Clipped inventory geometry: 214684.251689 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35386
- Blocks: 26504
- Forest area: 3184.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1877
- Scheduled area: 180.36 ha
- Eligible blocks (age class >= 40): 1877
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.81 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
