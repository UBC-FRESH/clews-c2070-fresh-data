# WS4 tiled 30-m dataset — G7|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G7|BC|S21` (parent `G7|BC`)
- Tile / row / col: `G7` / 2 / 1
- Province: `BC`
- Centroid: 51.744499, -116.702980
- Allocated harvest: 4305.478640 m3
- Productive subcell area: 6573.831484 ha
- Committed geometry area: 11804.752903 ha
- Clipped inventory geometry: 11804.752903 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 61823
- Blocks: 36717
- Forest area: 5564.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3463
- Scheduled area: 484.47 ha
- Eligible blocks (age class >= 40): 34623
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.27 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.30 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
