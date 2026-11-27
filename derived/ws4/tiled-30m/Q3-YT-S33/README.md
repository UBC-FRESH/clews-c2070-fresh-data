# WS4 tiled 30-m dataset — Q3|YT|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q3|YT|S33` (parent `Q3|YT`)
- Tile / row / col: `Q3` / 3 / 3
- Province: `YT`
- Centroid: 62.438193, -136.537764
- Allocated harvest: 255.809910 m3
- Productive subcell area: 171969.252036 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2476389
- Blocks: 732580
- Forest area: 222875.01 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 63221
- Scheduled area: 14540.40 ha
- Eligible blocks (age class >= 40): 632205
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.09 MB
- Schedules: 0.75 MB
- Runs: 0.00 MB
- Total: 27.84 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
