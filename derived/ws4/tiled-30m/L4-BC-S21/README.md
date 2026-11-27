# WS4 tiled 30-m dataset — L4|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L4|BC|S21` (parent `L4|BC`)
- Tile / row / col: `L4` / 2 / 1
- Province: `BC`
- Centroid: 56.522114, -127.772011
- Allocated harvest: 55114.838801 m3
- Productive subcell area: 155049.257483 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1932545
- Blocks: 1005002
- Forest area: 173929.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96251
- Scheduled area: 16598.16 ha
- Eligible blocks (age class >= 40): 962507
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.32 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 28.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
