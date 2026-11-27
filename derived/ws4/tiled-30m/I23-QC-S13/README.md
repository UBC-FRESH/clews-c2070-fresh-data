# WS4 tiled 30-m dataset — I23|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I23|QC|S13` (parent `I23|QC`)
- Tile / row / col: `I23` / 1 / 3
- Province: `QC`
- Centroid: 55.121326, -77.711440
- Allocated harvest: 15449.945877 m3
- Productive subcell area: 92882.994806 ha
- Committed geometry area: 193701.922679 ha
- Clipped inventory geometry: 193701.922679 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1203480
- Blocks: 493167
- Forest area: 108313.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40162
- Scheduled area: 9088.11 ha
- Eligible blocks (age class >= 40): 401613
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.59 MB
- Schedules: 0.47 MB
- Runs: 0.00 MB
- Total: 16.06 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
