# WS4 tiled 30-m dataset — D32|NS|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `D32|NS|S13` (parent `D32|NS`)
- Tile / row / col: `D32` / 1 / 3
- Province: `NS`
- Centroid: 44.396577, -64.333918
- Allocated harvest: 29394.408633 m3
- Productive subcell area: 50831.243950 ha
- Committed geometry area: 62420.532847 ha
- Clipped inventory geometry: 62420.532847 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 551095
- Blocks: 235431
- Forest area: 49598.55 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20167
- Scheduled area: 3924.63 ha
- Eligible blocks (age class >= 40): 201662
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.89 MB
- Schedules: 0.23 MB
- Runs: 0.00 MB
- Total: 8.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
