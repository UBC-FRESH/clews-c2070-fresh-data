# WS4 tiled 30-m dataset — H26|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H26|QC|S13` (parent `H26|QC`)
- Tile / row / col: `H26` / 1 / 3
- Province: `QC`
- Centroid: 52.577420, -71.880830
- Allocated harvest: 19944.756397 m3
- Productive subcell area: 131905.083658 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1741083
- Blocks: 385750
- Forest area: 156697.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 30882
- Scheduled area: 10486.62 ha
- Eligible blocks (age class >= 40): 308817
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.47 MB
- Schedules: 0.36 MB
- Runs: 0.00 MB
- Total: 17.83 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
