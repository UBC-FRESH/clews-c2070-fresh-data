# WS4 tiled 30-m dataset — K28|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K28|QC|S31` (parent `K28|QC`)
- Tile / row / col: `K28` / 3 / 1
- Province: `QC`
- Centroid: 56.453126, -65.526584
- Allocated harvest: 15232.710995 m3
- Productive subcell area: 118257.331241 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1293240
- Blocks: 644208
- Forest area: 116391.60 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 57479
- Scheduled area: 9920.34 ha
- Eligible blocks (age class >= 40): 574785
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.89 MB
- Schedules: 0.68 MB
- Runs: 0.00 MB
- Total: 18.57 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
