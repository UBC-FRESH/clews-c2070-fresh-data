# WS4 tiled 30-m dataset — K11|SK|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|SK|S23` (parent `K11|SK`)
- Tile / row / col: `K11` / 2 / 3
- Province: `SK`
- Centroid: 59.007053, -108.253461
- Allocated harvest: 13857.927805 m3
- Productive subcell area: 137192.076620 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1270915
- Blocks: 324352
- Forest area: 114382.35 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 23211
- Scheduled area: 10721.61 ha
- Eligible blocks (age class >= 40): 232107
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.16 MB
- Schedules: 0.27 MB
- Runs: 0.00 MB
- Total: 13.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
