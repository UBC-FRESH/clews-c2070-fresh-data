# WS4 tiled 30-m dataset — P11|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P11|NT|S13` (parent `P11|NT`)
- Tile / row / col: `P11` / 1 / 3
- Province: `NT`
- Centroid: 65.263763, -111.461986
- Allocated harvest: 12.923274 m3
- Productive subcell area: 36450.297906 ha
- Committed geometry area: 205711.332203 ha
- Clipped inventory geometry: 205711.332203 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 69576
- Blocks: 49076
- Forest area: 6261.84 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1480
- Scheduled area: 153.27 ha
- Eligible blocks (age class >= 40): 14796
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.51 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.53 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
