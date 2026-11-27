# WS4 tiled 30-m dataset — H23|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H23|QC|S31` (parent `H23|QC`)
- Tile / row / col: `H23` / 3 / 1
- Province: `QC`
- Centroid: 54.733996, -79.310524
- Allocated harvest: 1437.399021 m3
- Productive subcell area: 7814.170604 ha
- Committed geometry area: 15036.147139 ha
- Clipped inventory geometry: 15036.147139 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 18704
- Blocks: 7890
- Forest area: 1683.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 4549
- Scheduled area: 672.75 ha
- Eligible blocks (age class >= 40): 4549
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.36 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.41 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
