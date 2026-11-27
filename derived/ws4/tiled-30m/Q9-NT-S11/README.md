# WS4 tiled 30-m dataset — Q9|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S11` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 1 / 1
- Province: `NT`
- Centroid: 65.406332, -120.927888
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1590057
- Blocks: 697888
- Forest area: 143105.13 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63594
- Scheduled area: 12572.46 ha
- Eligible blocks (age class >= 40): 635931
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.32 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 22.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
