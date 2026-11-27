# WS4 tiled 30-m dataset — T7|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `T7|NT|S31` (parent `T7|NT`)
- Tile / row / col: `T7` / 3 / 1
- Province: `NT`
- Centroid: 68.517179, -133.428614
- Allocated harvest: 139.890227 m3
- Productive subcell area: 143690.950164 ha
- Committed geometry area: 243783.395198 ha
- Clipped inventory geometry: 243783.395198 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 714504
- Blocks: 321029
- Forest area: 64305.36 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20920
- Scheduled area: 4015.71 ha
- Eligible blocks (age class >= 40): 209194
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 9.81 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 10.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
