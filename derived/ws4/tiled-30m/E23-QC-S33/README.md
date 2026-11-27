# WS4 tiled 30-m dataset — E23|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E23|QC|S33` (parent `E23|QC`)
- Tile / row / col: `E23` / 3 / 3
- Province: `QC`
- Centroid: 50.752235, -79.416890
- Allocated harvest: 9803.331960 m3
- Productive subcell area: 41811.180938 ha
- Committed geometry area: 68624.567578 ha
- Clipped inventory geometry: 68624.567578 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 510829
- Blocks: 187985
- Forest area: 45974.61 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 16831
- Scheduled area: 3912.57 ha
- Eligible blocks (age class >= 40): 168303
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 6.78 MB
- Schedules: 0.19 MB
- Runs: 0.00 MB
- Total: 6.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
