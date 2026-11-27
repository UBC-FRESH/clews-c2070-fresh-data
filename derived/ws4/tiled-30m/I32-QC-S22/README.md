# WS4 tiled 30-m dataset — I32|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I32|QC|S22` (parent `I32|QC`)
- Tile / row / col: `I32` / 2 / 2
- Province: `QC`
- Centroid: 50.790434, -59.488196
- Allocated harvest: 34277.745598 m3
- Productive subcell area: 146979.025246 ha
- Committed geometry area: 208729.067906 ha
- Clipped inventory geometry: 208729.067906 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1392493
- Blocks: 545091
- Forest area: 125324.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46767
- Scheduled area: 10937.34 ha
- Eligible blocks (age class >= 40): 467662
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.05 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 18.60 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
