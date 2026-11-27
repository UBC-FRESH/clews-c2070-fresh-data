# WS4 tiled 30-m dataset — M12|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M12|NT|S32` (parent `M12|NT`)
- Tile / row / col: `M12` / 3 / 2
- Province: `NT`
- Centroid: 62.360970, -107.747011
- Allocated harvest: 33.870480 m3
- Productive subcell area: 93691.747566 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 753790
- Blocks: 450692
- Forest area: 67841.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32354
- Scheduled area: 4392.36 ha
- Eligible blocks (age class >= 40): 323532
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.75 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 12.13 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
