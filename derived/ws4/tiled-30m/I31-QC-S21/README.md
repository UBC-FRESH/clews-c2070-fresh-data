# WS4 tiled 30-m dataset — I31|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I31|QC|S21` (parent `I31|QC`)
- Tile / row / col: `I31` / 2 / 1
- Province: `QC`
- Centroid: 51.692824, -61.931070
- Allocated harvest: 58226.110202 m3
- Productive subcell area: 198609.088434 ha
- Committed geometry area: 249955.394783 ha
- Clipped inventory geometry: 249955.394783 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2535318
- Blocks: 651545
- Forest area: 228178.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 61977
- Scheduled area: 21470.94 ha
- Eligible blocks (age class >= 40): 619767
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.73 MB
- Schedules: 0.73 MB
- Runs: 0.00 MB
- Total: 28.47 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
