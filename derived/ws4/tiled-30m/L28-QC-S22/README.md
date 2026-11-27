# WS4 tiled 30-m dataset — L28|QC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `L28|QC|S22` (parent `L28|QC`)
- Tile / row / col: `L28` / 2 / 2
- Province: `QC`
- Centroid: 57.081824, -64.139313
- Allocated harvest: 3251.257884 m3
- Productive subcell area: 18536.095867 ha
- Committed geometry area: 172435.687700 ha
- Clipped inventory geometry: 172435.687700 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 13065
- Blocks: 8266
- Forest area: 1175.85 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 2355
- Scheduled area: 342.18 ha
- Eligible blocks (age class >= 40): 2355
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.32 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
