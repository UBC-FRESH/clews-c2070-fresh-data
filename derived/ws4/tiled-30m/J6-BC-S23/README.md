# WS4 tiled 30-m dataset — J6|BC|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J6|BC|S23` (parent `J6|BC`)
- Tile / row / col: `J6` / 2 / 3
- Province: `BC`
- Centroid: 55.681172, -120.080623
- Allocated harvest: 14443.604065 m3
- Productive subcell area: 25663.664523 ha
- Committed geometry area: 30592.037866 ha
- Clipped inventory geometry: 30592.037866 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 165229
- Blocks: 67920
- Forest area: 14870.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 5915
- Scheduled area: 1294.92 ha
- Eligible blocks (age class >= 40): 59146
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.69 MB
- Schedules: 0.06 MB
- Runs: 0.00 MB
- Total: 2.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
