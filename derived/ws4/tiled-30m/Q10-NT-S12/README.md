# WS4 tiled 30-m dataset — Q10|NT|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q10|NT|S12` (parent `Q10|NT`)
- Tile / row / col: `Q10` / 1 / 2
- Province: `NT`
- Centroid: 66.083665, -116.741978
- Allocated harvest: 35.330298 m3
- Productive subcell area: 82136.501364 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1302150
- Blocks: 510364
- Forest area: 117193.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34762
- Scheduled area: 7615.53 ha
- Eligible blocks (age class >= 40): 347614
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.52 MB
- Schedules: 0.41 MB
- Runs: 0.00 MB
- Total: 16.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
