# WS4 tiled 30-m dataset — K11|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|SK|S31` (parent `K11|SK`)
- Tile / row / col: `K11` / 3 / 1
- Province: `SK`
- Centroid: 59.257278, -109.874416
- Allocated harvest: 3722.668115 m3
- Productive subcell area: 36854.035934 ha
- Committed geometry area: 67157.733964 ha
- Clipped inventory geometry: 67157.733964 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 162043
- Blocks: 34289
- Forest area: 14583.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1994
- Scheduled area: 380.70 ha
- Eligible blocks (age class >= 40): 19934
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.90 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
