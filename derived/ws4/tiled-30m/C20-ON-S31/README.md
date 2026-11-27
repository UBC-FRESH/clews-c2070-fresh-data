# WS4 tiled 30-m dataset — C20|ON|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C20|ON|S31` (parent `C20|ON`)
- Tile / row / col: `C20` / 3 / 1
- Province: `ON`
- Centroid: 48.986615, -87.966089
- Allocated harvest: 45063.268035 m3
- Productive subcell area: 158196.733109 ha
- Committed geometry area: 187651.195680 ha
- Clipped inventory geometry: 187651.195680 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1883839
- Blocks: 705897
- Forest area: 169545.51 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 65244
- Scheduled area: 14931.72 ha
- Eligible blocks (age class >= 40): 652436
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.55 MB
- Schedules: 0.77 MB
- Runs: 0.00 MB
- Total: 24.33 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
