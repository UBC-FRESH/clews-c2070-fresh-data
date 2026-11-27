# WS4 tiled 30-m dataset — Q10|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q10|NT|S33` (parent `Q10|NT`)
- Tile / row / col: `Q10` / 3 / 3
- Province: `NT`
- Centroid: 66.830293, -116.769723
- Allocated harvest: 0.091900 m3
- Productive subcell area: 213.650721 ha
- Committed geometry area: 650.291640 ha
- Clipped inventory geometry: 650.291640 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1940
- Blocks: 1007
- Forest area: 174.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 664
- Scheduled area: 133.47 ha
- Eligible blocks (age class >= 40): 664
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.10 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.10 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
