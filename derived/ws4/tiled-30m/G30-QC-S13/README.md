# WS4 tiled 30-m dataset — G30|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G30|QC|S13` (parent `G30|QC`)
- Tile / row / col: `G30` / 1 / 3
- Province: `QC`
- Centroid: 49.048651, -64.958178
- Allocated harvest: 60462.946870 m3
- Productive subcell area: 136280.026800 ha
- Committed geometry area: 156376.475190 ha
- Clipped inventory geometry: 156376.475190 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1622709
- Blocks: 605580
- Forest area: 146043.81 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 51667
- Scheduled area: 10816.29 ha
- Eligible blocks (age class >= 40): 516662
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.31 MB
- Schedules: 0.61 MB
- Runs: 0.00 MB
- Total: 20.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
