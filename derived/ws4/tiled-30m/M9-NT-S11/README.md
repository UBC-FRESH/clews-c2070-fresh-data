# WS4 tiled 30-m dataset — M9|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|NT|S11` (parent `M9|NT`)
- Tile / row / col: `M9` / 1 / 1
- Province: `NT`
- Centroid: 60.242212, -116.501152
- Allocated harvest: 134.751345 m3
- Productive subcell area: 106534.581155 ha
- Committed geometry area: 243340.534683 ha
- Clipped inventory geometry: 243340.534683 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1228091
- Blocks: 422759
- Forest area: 110528.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31540
- Scheduled area: 7733.52 ha
- Eligible blocks (age class >= 40): 315400
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.48 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 14.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
