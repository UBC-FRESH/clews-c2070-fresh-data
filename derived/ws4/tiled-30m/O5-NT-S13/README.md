# WS4 tiled 30-m dataset — O5|NT|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `O5|NT|S13` (parent `O5|NT`)
- Tile / row / col: `O5` / 1 / 3
- Province: `NT`
- Centroid: 60.809568, -126.811501
- Allocated harvest: 1.201583 m3
- Productive subcell area: 1519.399077 ha
- Committed geometry area: 3665.048710 ha
- Clipped inventory geometry: 3665.048710 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 35993
- Blocks: 16478
- Forest area: 3239.37 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1572
- Scheduled area: 304.83 ha
- Eligible blocks (age class >= 40): 15717
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.69 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.70 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
