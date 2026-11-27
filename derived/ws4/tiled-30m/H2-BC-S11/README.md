# WS4 tiled 30-m dataset — H2|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S11` (parent `H2|BC`)
- Tile / row / col: `H2` / 1 / 1
- Province: `BC`
- Centroid: 50.045594, -126.911857
- Allocated harvest: 147716.813980 m3
- Productive subcell area: 168357.494303 ha
- Committed geometry area: 202866.663212 ha
- Clipped inventory geometry: 202866.663212 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2131032
- Blocks: 866127
- Forest area: 191792.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 84860
- Scheduled area: 15183.90 ha
- Eligible blocks (age class >= 40): 848591
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.26 MB
- Schedules: 1.01 MB
- Runs: 0.00 MB
- Total: 27.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
