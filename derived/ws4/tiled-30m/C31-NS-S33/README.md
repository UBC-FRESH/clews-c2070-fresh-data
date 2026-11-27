# WS4 tiled 30-m dataset — C31|NS|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C31|NS|S33` (parent `C31|NS`)
- Tile / row / col: `C31` / 3 / 3
- Province: `NS`
- Centroid: 44.458701, -65.922439
- Allocated harvest: 37056.669303 m3
- Productive subcell area: 66214.441868 ha
- Committed geometry area: 80595.404584 ha
- Clipped inventory geometry: 80595.404584 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 741721
- Blocks: 249502
- Forest area: 66754.89 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20077
- Scheduled area: 4611.15 ha
- Eligible blocks (age class >= 40): 200769
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.26 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 9.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
