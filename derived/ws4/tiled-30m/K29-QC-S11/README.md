# WS4 tiled 30-m dataset — K29|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|QC|S11` (parent `K29|QC`)
- Tile / row / col: `K29` / 1 / 1
- Province: `QC`
- Centroid: 55.012142, -64.110615
- Allocated harvest: 19310.523085 m3
- Productive subcell area: 117284.046212 ha
- Committed geometry area: 242383.316425 ha
- Clipped inventory geometry: 242383.316425 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1208691
- Blocks: 754535
- Forest area: 108782.19 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 66981
- Scheduled area: 9316.35 ha
- Eligible blocks (age class >= 40): 669808
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 19.14 MB
- Schedules: 0.79 MB
- Runs: 0.00 MB
- Total: 19.93 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
