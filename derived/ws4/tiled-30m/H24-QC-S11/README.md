# WS4 tiled 30-m dataset — H24|QC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H24|QC|S11` (parent `H24|QC`)
- Tile / row / col: `H24` / 1 / 1
- Province: `QC`
- Centroid: 53.718997, -77.641759
- Allocated harvest: 27409.990069 m3
- Productive subcell area: 129578.173407 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1511661
- Blocks: 583640
- Forest area: 136049.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 48281
- Scheduled area: 9718.74 ha
- Eligible blocks (age class >= 40): 482806
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 18.78 MB
- Schedules: 0.57 MB
- Runs: 0.00 MB
- Total: 19.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
