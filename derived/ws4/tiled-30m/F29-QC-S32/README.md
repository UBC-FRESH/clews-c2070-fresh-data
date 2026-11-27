# WS4 tiled 30-m dataset — F29|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F29|QC|S32` (parent `F29|QC`)
- Tile / row / col: `F29` / 3 / 2
- Province: `QC`
- Centroid: 49.523633, -67.696905
- Allocated harvest: 89970.376243 m3
- Productive subcell area: 195350.534786 ha
- Committed geometry area: 232694.083539 ha
- Clipped inventory geometry: 232694.083539 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2329396
- Blocks: 908580
- Forest area: 209645.64 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 85525
- Scheduled area: 19450.89 ha
- Eligible blocks (age class >= 40): 855242
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.27 MB
- Schedules: 1.02 MB
- Runs: 0.00 MB
- Total: 30.29 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
