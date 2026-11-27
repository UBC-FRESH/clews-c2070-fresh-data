# WS4 tiled 30-m dataset — H29|QC|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H29|QC|S13` (parent `H29|QC`)
- Tile / row / col: `H29` / 1 / 3
- Province: `QC`
- Centroid: 50.944071, -65.844641
- Allocated harvest: 52017.929550 m3
- Productive subcell area: 182295.005519 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2181301
- Blocks: 622082
- Forest area: 196317.09 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 53864
- Scheduled area: 16046.46 ha
- Eligible blocks (age class >= 40): 538640
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 24.39 MB
- Schedules: 0.64 MB
- Runs: 0.00 MB
- Total: 25.03 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
