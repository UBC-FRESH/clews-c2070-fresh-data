# WS4 tiled 30-m dataset — H28|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H28|QC|S33` (parent `H28|QC`)
- Tile / row / col: `H28` / 3 / 3
- Province: `QC`
- Centroid: 52.351318, -67.185086
- Allocated harvest: 37533.593791 m3
- Productive subcell area: 166643.975505 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1825414
- Blocks: 614889
- Forest area: 164287.26 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 54221
- Scheduled area: 13748.58 ha
- Eligible blocks (age class >= 40): 542207
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.33 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 21.97 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
