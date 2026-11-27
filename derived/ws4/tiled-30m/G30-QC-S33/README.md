# WS4 tiled 30-m dataset — G30|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G30|QC|S33` (parent `G30|QC`)
- Tile / row / col: `G30` / 3 / 3
- Province: `QC`
- Centroid: 49.846973, -64.193962
- Allocated harvest: 26858.291879 m3
- Productive subcell area: 60537.054949 ha
- Committed geometry area: 69464.113661 ha
- Clipped inventory geometry: 69464.113661 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 657755
- Blocks: 207683
- Forest area: 59197.95 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 19230
- Scheduled area: 4527.81 ha
- Eligible blocks (age class >= 40): 192300
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 8.15 MB
- Schedules: 0.22 MB
- Runs: 0.00 MB
- Total: 8.37 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
