# WS4 tiled 30-m dataset — L9|NT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L9|NT|S33` (parent `L9|NT`)
- Tile / row / col: `L9` / 3 / 3
- Province: `NT`
- Centroid: 60.157729, -114.461917
- Allocated harvest: 168.337800 m3
- Productive subcell area: 110817.351903 ha
- Committed geometry area: 175418.439908 ha
- Clipped inventory geometry: 175418.439908 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1330618
- Blocks: 438472
- Forest area: 119755.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 34018
- Scheduled area: 8618.85 ha
- Eligible blocks (age class >= 40): 340172
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.65 MB
- Schedules: 0.40 MB
- Runs: 0.00 MB
- Total: 16.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
