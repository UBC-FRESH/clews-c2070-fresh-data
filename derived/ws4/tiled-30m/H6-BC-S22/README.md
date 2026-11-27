# WS4 tiled 30-m dataset — H6|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H6|BC|S22` (parent `H6|BC`)
- Tile / row / col: `H6` / 2 / 2
- Province: `BC`
- Centroid: 52.888389, -118.807021
- Allocated harvest: 56318.712921 m3
- Productive subcell area: 95489.274861 ha
- Committed geometry area: 160535.377035 ha
- Clipped inventory geometry: 160535.377035 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 951531
- Blocks: 543949
- Forest area: 85637.79 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51300
- Scheduled area: 7592.76 ha
- Eligible blocks (age class >= 40): 512995
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.45 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 15.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
