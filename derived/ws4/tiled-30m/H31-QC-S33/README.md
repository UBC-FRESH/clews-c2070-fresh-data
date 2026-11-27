# WS4 tiled 30-m dataset — H31|QC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H31|QC|S33` (parent `H31|QC`)
- Tile / row / col: `H31` / 3 / 3
- Province: `QC`
- Centroid: 50.458072, -61.406739
- Allocated harvest: 54760.076181 m3
- Productive subcell area: 177926.167458 ha
- Committed geometry area: 247776.952850 ha
- Clipped inventory geometry: 247776.952850 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1436890
- Blocks: 605267
- Forest area: 129320.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 52682
- Scheduled area: 12110.31 ha
- Eligible blocks (age class >= 40): 526820
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.03 MB
- Schedules: 0.62 MB
- Runs: 0.00 MB
- Total: 19.65 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
