# WS4 tiled 30-m dataset — F13|SK|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F13|SK|S22` (parent `F13|SK`)
- Tile / row / col: `F13` / 2 / 2
- Province: `SK`
- Centroid: 52.581259, -102.273809
- Allocated harvest: 44409.646743 m3
- Productive subcell area: 179342.960330 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2203587
- Blocks: 827778
- Forest area: 198322.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78131
- Scheduled area: 17547.48 ha
- Eligible blocks (age class >= 40): 781305
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.34 MB
- Schedules: 0.93 MB
- Runs: 0.00 MB
- Total: 28.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
