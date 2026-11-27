# WS4 tiled 30-m dataset — J14|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J14|SK|S21` (parent `J14|SK`)
- Tile / row / col: `J14` / 2 / 1
- Province: `SK`
- Centroid: 58.147354, -102.089624
- Allocated harvest: 2290.689036 m3
- Productive subcell area: 26956.060893 ha
- Committed geometry area: 47017.418306 ha
- Clipped inventory geometry: 47017.418306 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 242863
- Blocks: 62417
- Forest area: 21857.67 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4782
- Scheduled area: 1198.98 ha
- Eligible blocks (age class >= 40): 47811
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.97 MB
- Schedules: 0.05 MB
- Runs: 0.00 MB
- Total: 3.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
