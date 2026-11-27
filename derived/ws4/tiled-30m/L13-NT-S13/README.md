# WS4 tiled 30-m dataset — L13|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L13|NT|S13` (parent `L13|NT`)
- Tile / row / col: `L13` / 1 / 3
- Province: `NT`
- Centroid: 60.382075, -103.156842
- Allocated harvest: 40.712733 m3
- Productive subcell area: 104674.290360 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1274060
- Blocks: 383652
- Forest area: 114665.40 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30518
- Scheduled area: 7632.90 ha
- Eligible blocks (age class >= 40): 305172
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.48 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 14.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
