# WS4 tiled 30-m dataset — E28|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E28|QC|S13` (parent `E28|QC`)
- Tile / row / col: `E28` / 1 / 3
- Province: `QC`
- Centroid: 47.817480, -70.293613
- Allocated harvest: 96740.053363 m3
- Productive subcell area: 198703.405761 ha
- Committed geometry area: 233632.254808 ha
- Clipped inventory geometry: 233632.254808 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2346945
- Blocks: 859007
- Forest area: 211225.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 76794
- Scheduled area: 18037.89 ha
- Eligible blocks (age class >= 40): 767936
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.21 MB
- Schedules: 0.91 MB
- Runs: 0.00 MB
- Total: 30.12 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
