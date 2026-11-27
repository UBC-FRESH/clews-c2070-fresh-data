# WS4 tiled 30-m dataset — L11|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L11|NT|S31` (parent `L11|NT`)
- Tile / row / col: `L11` / 3 / 1
- Province: `NT`
- Centroid: 60.596083, -110.869757
- Allocated harvest: 106.464871 m3
- Productive subcell area: 150185.735956 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1425966
- Blocks: 316992
- Forest area: 128336.94 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 11391
- Scheduled area: 7203.60 ha
- Eligible blocks (age class >= 40): 113905
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.90 MB
- Schedules: 0.13 MB
- Runs: 0.00 MB
- Total: 14.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
