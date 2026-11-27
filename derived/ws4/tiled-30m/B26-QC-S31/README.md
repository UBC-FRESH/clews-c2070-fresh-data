# WS4 tiled 30-m dataset — B26|QC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `B26|QC|S31` (parent `B26|QC`)
- Tile / row / col: `B26` / 3 / 1
- Province: `QC`
- Centroid: 46.044671, -76.703100
- Allocated harvest: 118183.335645 m3
- Productive subcell area: 195982.959506 ha
- Committed geometry area: 243441.540998 ha
- Clipped inventory geometry: 243441.540998 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2337106
- Blocks: 636428
- Forest area: 210339.54 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 59819
- Scheduled area: 18989.46 ha
- Eligible blocks (age class >= 40): 598190
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.22 MB
- Schedules: 0.71 MB
- Runs: 0.00 MB
- Total: 26.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
