# WS4 tiled 30-m dataset — T8|NT|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T8|NT|S32` (parent `T8|NT`)
- Tile / row / col: `T8` / 3 / 2
- Province: `NT`
- Centroid: 69.505154, -129.100262
- Allocated harvest: 5.062796 m3
- Productive subcell area: 11199.940353 ha
- Committed geometry area: 237694.577241 ha
- Clipped inventory geometry: 237694.577241 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 121668
- Blocks: 78938
- Forest area: 10950.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1815
- Scheduled area: 193.77 ha
- Eligible blocks (age class >= 40): 18144
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 2.50 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 2.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
