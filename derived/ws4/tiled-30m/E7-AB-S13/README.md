# WS4 tiled 30-m dataset — E7|AB|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E7|AB|S13` (parent `E7|AB`)
- Tile / row / col: `E7` / 1 / 3
- Province: `AB`
- Centroid: 49.243016, -113.624984
- Allocated harvest: 116080.108226 m3
- Productive subcell area: 112478.777767 ha
- Committed geometry area: 246603.210989 ha
- Clipped inventory geometry: 246603.210989 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 479791
- Blocks: 232735
- Forest area: 43181.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17830
- Scheduled area: 3554.91 ha
- Eligible blocks (age class >= 40): 178292
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.30 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.50 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
