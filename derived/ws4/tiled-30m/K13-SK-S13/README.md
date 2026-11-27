# WS4 tiled 30-m dataset — K13|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S13` (parent `K13|SK`)
- Tile / row / col: `K13` / 1 / 3
- Province: `SK`
- Centroid: 59.008341, -102.813838
- Allocated harvest: 13404.703615 m3
- Productive subcell area: 141643.458128 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1587386
- Blocks: 372997
- Forest area: 142864.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25733
- Scheduled area: 6421.68 ha
- Eligible blocks (age class >= 40): 257327
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.98 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 16.28 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
