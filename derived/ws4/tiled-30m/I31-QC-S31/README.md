# WS4 tiled 30-m dataset — I31|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|QC|S31` (parent `I31|QC`)
- Tile / row / col: `I31` / 3 / 1
- Province: `QC`
- Centroid: 51.923100, -61.567720
- Allocated harvest: 15861.689162 m3
- Productive subcell area: 54104.174478 ha
- Committed geometry area: 68091.699114 ha
- Clipped inventory geometry: 68091.699114 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 610305
- Blocks: 188933
- Forest area: 54927.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 18222
- Scheduled area: 5383.98 ha
- Eligible blocks (age class >= 40): 182216
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 7.65 MB
- Schedules: 0.21 MB
- Runs: 0.00 MB
- Total: 7.86 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
