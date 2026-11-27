# WS4 tiled 30-m dataset — G11|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G11|SK|S33` (parent `G11|SK`)
- Tile / row / col: `G11` / 3 / 3
- Province: `SK`
- Centroid: 54.050798, -106.486944
- Allocated harvest: 32819.653730 m3
- Productive subcell area: 139868.653356 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2261301
- Blocks: 995790
- Forest area: 203517.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 95883
- Scheduled area: 18641.52 ha
- Eligible blocks (age class >= 40): 958825
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 30.15 MB
- Schedules: 1.14 MB
- Runs: 0.00 MB
- Total: 31.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
