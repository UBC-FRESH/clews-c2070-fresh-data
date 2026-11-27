# WS4 tiled 30-m dataset — F30|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F30|QC|S31` (parent `F30|QC`)
- Tile / row / col: `F30` / 3 / 1
- Province: `QC`
- Centroid: 49.035255, -66.401227
- Allocated harvest: 71733.752496 m3
- Productive subcell area: 133125.415682 ha
- Committed geometry area: 140929.485598 ha
- Clipped inventory geometry: 140929.485598 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1441778
- Blocks: 443466
- Forest area: 129760.02 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 38442
- Scheduled area: 10774.89 ha
- Eligible blocks (age class >= 40): 384411
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.03 MB
- Schedules: 0.45 MB
- Runs: 0.00 MB
- Total: 17.48 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
