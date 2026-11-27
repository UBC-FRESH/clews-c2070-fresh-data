# WS4 tiled 30-m dataset — Q9|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q9|NT|S32` (parent `Q9|NT`)
- Tile / row / col: `Q9` / 3 / 2
- Province: `NT`
- Centroid: 66.438447, -120.783303
- Allocated harvest: 45.367961 m3
- Productive subcell area: 76940.164223 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 31724
- Blocks: 13982
- Forest area: 2855.16 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 848
- Scheduled area: 162.81 ha
- Eligible blocks (age class >= 40): 8475
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.58 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.59 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
