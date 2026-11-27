# WS4 tiled 30-m dataset — I4|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I4|BC|S33` (parent `I4|BC`)
- Tile / row / col: `I4` / 3 / 3
- Province: `BC`
- Centroid: 53.696352, -123.399266
- Allocated harvest: 121739.863305 m3
- Productive subcell area: 226249.614180 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2614134
- Blocks: 894822
- Forest area: 235272.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 73174
- Scheduled area: 12953.07 ha
- Eligible blocks (age class >= 40): 731736
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.41 MB
- Schedules: 0.87 MB
- Runs: 0.00 MB
- Total: 31.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
