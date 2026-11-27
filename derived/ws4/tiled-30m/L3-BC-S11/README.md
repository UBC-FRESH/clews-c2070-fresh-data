# WS4 tiled 30-m dataset — L3|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L3|BC|S11` (parent `L3|BC`)
- Tile / row / col: `L3` / 1 / 1
- Province: `BC`
- Centroid: 55.433233, -129.462656
- Allocated harvest: 73923.229835 m3
- Productive subcell area: 133899.138572 ha
- Committed geometry area: 234974.286163 ha
- Clipped inventory geometry: 234974.286163 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1462571
- Blocks: 811035
- Forest area: 131631.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 77846
- Scheduled area: 11912.85 ha
- Eligible blocks (age class >= 40): 778451
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.47 MB
- Schedules: 0.92 MB
- Runs: 0.00 MB
- Total: 22.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
