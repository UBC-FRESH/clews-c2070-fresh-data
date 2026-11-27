# WS4 tiled 30-m dataset — F14|MB|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F14|MB|S31` (parent `F14|MB`)
- Tile / row / col: `F14` / 3 / 1
- Province: `MB`
- Centroid: 53.127970, -100.854982
- Allocated harvest: 5981.286535 m3
- Productive subcell area: 126848.865485 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1521338
- Blocks: 443416
- Forest area: 136920.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 41518
- Scheduled area: 13888.89 ha
- Eligible blocks (age class >= 40): 415172
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.55 MB
- Schedules: 0.49 MB
- Runs: 0.00 MB
- Total: 18.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
