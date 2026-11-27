# WS4 tiled 30-m dataset — M8|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M8|NT|S13` (parent `M8|NT`)
- Tile / row / col: `M8` / 1 / 3
- Province: `NT`
- Centroid: 60.151781, -117.387388
- Allocated harvest: 105.055140 m3
- Productive subcell area: 75537.595454 ha
- Committed geometry area: 170263.225555 ha
- Clipped inventory geometry: 170263.225555 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 905212
- Blocks: 326221
- Forest area: 81469.08 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25932
- Scheduled area: 5549.04 ha
- Eligible blocks (age class >= 40): 259315
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.24 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 11.54 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
