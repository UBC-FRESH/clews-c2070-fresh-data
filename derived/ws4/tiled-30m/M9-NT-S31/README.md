# WS4 tiled 30-m dataset — M9|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M9|NT|S31` (parent `M9|NT`)
- Tile / row / col: `M9` / 3 / 1
- Province: `NT`
- Centroid: 61.105405, -117.139767
- Allocated harvest: 138.439066 m3
- Productive subcell area: 109450.097673 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1348966
- Blocks: 535277
- Forest area: 121406.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 46478
- Scheduled area: 9816.48 ha
- Eligible blocks (age class >= 40): 464780
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.39 MB
- Schedules: 0.55 MB
- Runs: 0.00 MB
- Total: 17.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
