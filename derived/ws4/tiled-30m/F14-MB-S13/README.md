# WS4 tiled 30-m dataset — F14|MB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F14|MB|S13` (parent `F14|MB`)
- Tile / row / col: `F14` / 1 / 3
- Province: `MB`
- Centroid: 52.292733, -99.242163
- Allocated harvest: 5981.286535 m3
- Productive subcell area: 126848.865485 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1161123
- Blocks: 491865
- Forest area: 104501.07 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 43079
- Scheduled area: 9566.82 ha
- Eligible blocks (age class >= 40): 430787
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.60 MB
- Schedules: 0.51 MB
- Runs: 0.00 MB
- Total: 16.11 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
