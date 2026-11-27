# WS4 tiled 30-m dataset — K13|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|NT|S31` (parent `K13|NT`)
- Tile / row / col: `K13` / 3 / 1
- Province: `NT`
- Centroid: 60.019567, -104.713364
- Allocated harvest: 3.696950 m3
- Productive subcell area: 6814.118388 ha
- Committed geometry area: 12898.254905 ha
- Clipped inventory geometry: 12898.254905 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 50768
- Blocks: 14637
- Forest area: 4569.12 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1317
- Scheduled area: 352.53 ha
- Eligible blocks (age class >= 40): 13170
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.74 MB
- Schedules: 0.01 MB
- Runs: 0.00 MB
- Total: 0.75 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
