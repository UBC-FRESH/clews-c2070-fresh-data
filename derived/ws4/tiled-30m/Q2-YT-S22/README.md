# WS4 tiled 30-m dataset — Q2|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q2|YT|S22` (parent `Q2|YT`)
- Tile / row / col: `Q2` / 2 / 2
- Province: `YT`
- Centroid: 60.924506, -138.977688
- Allocated harvest: 80.784582 m3
- Productive subcell area: 55569.557154 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 91788
- Blocks: 48811
- Forest area: 8260.92 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3406
- Scheduled area: 547.47 ha
- Eligible blocks (age class >= 40): 34051
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.76 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 1.79 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
