# WS4 tiled 30-m dataset — L3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L3|BC|S31` (parent `L3|BC`)
- Tile / row / col: `L3` / 3 / 1
- Province: `BC`
- Centroid: 56.279901, -130.227967
- Allocated harvest: 48210.032712 m3
- Productive subcell area: 87324.131604 ha
- Committed geometry area: 153241.654184 ha
- Clipped inventory geometry: 153241.654184 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 259934
- Blocks: 147143
- Forest area: 23394.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 12825
- Scheduled area: 1863.27 ha
- Eligible blocks (age class >= 40): 128246
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.71 MB
- Schedules: 0.14 MB
- Runs: 0.00 MB
- Total: 4.85 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
