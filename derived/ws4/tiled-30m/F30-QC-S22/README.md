# WS4 tiled 30-m dataset — F30|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S22` (parent `F30|QC`)
- Tile / row / col: `F30` / 2 / 2
- Province: `QC`
- Centroid: 48.523536, -66.127663
- Allocated harvest: 127251.142994 m3
- Productive subcell area: 236156.073225 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2716164
- Blocks: 905671
- Forest area: 244454.76 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 78879
- Scheduled area: 18762.48 ha
- Eligible blocks (age class >= 40): 788788
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 32.06 MB
- Schedules: 0.94 MB
- Runs: 0.00 MB
- Total: 32.99 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
