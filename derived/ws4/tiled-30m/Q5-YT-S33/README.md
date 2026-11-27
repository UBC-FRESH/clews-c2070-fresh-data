# WS4 tiled 30-m dataset — Q5|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q5|YT|S33` (parent `Q5|YT`)
- Tile / row / col: `Q5` / 3 / 3
- Province: `YT`
- Centroid: 64.037437, -131.502919
- Allocated harvest: 172.430795 m3
- Productive subcell area: 153753.100446 ha
- Committed geometry area: 249999.370450 ha
- Clipped inventory geometry: 249999.370450 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 543206
- Blocks: 248914
- Forest area: 48888.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 14953
- Scheduled area: 2953.71 ha
- Eligible blocks (age class >= 40): 149530
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.87 MB
- Schedules: 0.17 MB
- Runs: 0.00 MB
- Total: 8.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
