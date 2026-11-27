# WS4 tiled 30-m dataset — R4|YT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `R4|YT|S31` (parent `R4|YT`)
- Tile / row / col: `R4` / 3 / 1
- Province: `YT`
- Centroid: 63.817520, -137.614930
- Allocated harvest: 337.589146 m3
- Productive subcell area: 176424.897866 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2209371
- Blocks: 644847
- Forest area: 198843.39 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53171
- Scheduled area: 14106.24 ha
- Eligible blocks (age class >= 40): 531705
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.44 MB
- Schedules: 0.63 MB
- Runs: 0.00 MB
- Total: 25.07 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
