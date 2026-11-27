# WS4 tiled 30-m dataset — E13|MB|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E13|MB|S23` (parent `E13|MB`)
- Tile / row / col: `E13` / 2 / 3
- Province: `MB`
- Centroid: 51.277028, -101.250440
- Allocated harvest: 6332.439937 m3
- Productive subcell area: 128696.528671 ha
- Committed geometry area: 209574.234699 ha
- Clipped inventory geometry: 209574.234699 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 714095
- Blocks: 280847
- Forest area: 64268.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 24139
- Scheduled area: 5337.09 ha
- Eligible blocks (age class >= 40): 241385
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.46 MB
- Schedules: 0.28 MB
- Runs: 0.00 MB
- Total: 9.74 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
