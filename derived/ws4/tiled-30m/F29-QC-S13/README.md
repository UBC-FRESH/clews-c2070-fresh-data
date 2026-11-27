# WS4 tiled 30-m dataset — F29|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S13` (parent `F29|QC`)
- Tile / row / col: `F29` / 1 / 3
- Province: `QC`
- Centroid: 48.499816, -67.636536
- Allocated harvest: 95940.039853 m3
- Productive subcell area: 208312.323181 ha
- Committed geometry area: 248133.669997 ha
- Clipped inventory geometry: 248133.669997 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2228902
- Blocks: 799178
- Forest area: 200601.18 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66727
- Scheduled area: 16188.12 ha
- Eligible blocks (age class >= 40): 667264
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.29 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 28.08 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
