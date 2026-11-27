# WS4 tiled 30-m dataset — J26|QC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J26|QC|S12` (parent `J26|QC`)
- Tile / row / col: `J26` / 1 / 2
- Province: `QC`
- Centroid: 55.296147, -70.918544
- Allocated harvest: 13507.774698 m3
- Productive subcell area: 127798.873441 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1454020
- Blocks: 594647
- Forest area: 130861.80 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 49926
- Scheduled area: 11676.15 ha
- Eligible blocks (age class >= 40): 499260
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.84 MB
- Schedules: 0.59 MB
- Runs: 0.00 MB
- Total: 19.43 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
