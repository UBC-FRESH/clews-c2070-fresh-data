# WS4 tiled 30-m dataset — R2|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R2|YT|S33` (parent `R2|YT`)
- Tile / row / col: `R2` / 3 / 3
- Province: `YT`
- Centroid: 62.631628, -140.652244
- Allocated harvest: 210.238076 m3
- Productive subcell area: 99740.202040 ha
- Committed geometry area: 193535.636640 ha
- Clipped inventory geometry: 193535.636640 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1740396
- Blocks: 689666
- Forest area: 156635.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 62488
- Scheduled area: 13062.15 ha
- Eligible blocks (age class >= 40): 624878
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.20 MB
- Schedules: 0.74 MB
- Runs: 0.00 MB
- Total: 22.94 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
