# WS4 tiled 30-m dataset — C18|ON|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `C18|ON|S11` (parent `C18|ON`)
- Tile / row / col: `C18` / 1 / 1
- Province: `ON`
- Centroid: 48.388466, -92.098695
- Allocated harvest: 18221.558227 m3
- Productive subcell area: 84234.631276 ha
- Committed geometry area: 105992.239052 ha
- Clipped inventory geometry: 105992.239052 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 947638
- Blocks: 398276
- Forest area: 85287.42 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36414
- Scheduled area: 7209.81 ha
- Eligible blocks (age class >= 40): 364140
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.61 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 13.04 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
