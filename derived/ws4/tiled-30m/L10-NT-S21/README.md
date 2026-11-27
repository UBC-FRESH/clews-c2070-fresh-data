# WS4 tiled 30-m dataset — L10|NT|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|NT|S21` (parent `L10|NT`)
- Tile / row / col: `L10` / 2 / 1
- Province: `NT`
- Centroid: 60.023438, -113.137437
- Allocated harvest: 10.260092 m3
- Productive subcell area: 6423.367953 ha
- Committed geometry area: 10387.439916 ha
- Clipped inventory geometry: 10387.439916 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 103427
- Blocks: 33710
- Forest area: 9308.43 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3187
- Scheduled area: 691.56 ha
- Eligible blocks (age class >= 40): 31862
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.52 MB
- Schedules: 0.03 MB
- Runs: 0.00 MB
- Total: 1.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
