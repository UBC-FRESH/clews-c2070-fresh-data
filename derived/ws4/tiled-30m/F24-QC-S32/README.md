# WS4 tiled 30-m dataset — F24|QC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F24|QC|S32` (parent `F24|QC`)
- Tile / row / col: `F24` / 3 / 2
- Province: `QC`
- Centroid: 51.842935, -77.726123
- Allocated harvest: 31114.661903 m3
- Productive subcell area: 152592.932984 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1669380
- Blocks: 419609
- Forest area: 150244.20 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 28588
- Scheduled area: 6575.76 ha
- Eligible blocks (age class >= 40): 285873
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.14 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 17.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
