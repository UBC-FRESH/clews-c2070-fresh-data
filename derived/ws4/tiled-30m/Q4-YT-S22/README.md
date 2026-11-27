# WS4 tiled 30-m dataset — Q4|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q4|YT|S22` (parent `Q4|YT`)
- Tile / row / col: `Q4` / 2 / 2
- Province: `YT`
- Centroid: 62.615300, -134.331991
- Allocated harvest: 327.910389 m3
- Productive subcell area: 191647.548919 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2082597
- Blocks: 799762
- Forest area: 187433.73 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 69760
- Scheduled area: 14730.48 ha
- Eligible blocks (age class >= 40): 697599
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.73 MB
- Schedules: 0.83 MB
- Runs: 0.00 MB
- Total: 26.56 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
