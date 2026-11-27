# WS4 tiled 30-m dataset — L10|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L10|NT|S31` (parent `L10|NT`)
- Tile / row / col: `L10` / 3 / 1
- Province: `NT`
- Centroid: 60.233877, -113.563269
- Allocated harvest: 238.732106 m3
- Productive subcell area: 149459.110973 ha
- Committed geometry area: 241695.251838 ha
- Clipped inventory geometry: 241695.251838 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1607854
- Blocks: 632026
- Forest area: 144706.86 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45142
- Scheduled area: 10128.87 ha
- Eligible blocks (age class >= 40): 451415
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.98 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 20.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
