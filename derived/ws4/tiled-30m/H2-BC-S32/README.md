# WS4 tiled 30-m dataset — H2|BC|S32

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H2|BC|S32` (parent `H2|BC`)
- Tile / row / col: `H2` / 3 / 2
- Province: `BC`
- Centroid: 51.054635, -126.989529
- Allocated harvest: 140759.211265 m3
- Productive subcell area: 160427.695874 ha
- Committed geometry area: 193311.450039 ha
- Clipped inventory geometry: 193311.450039 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1960290
- Blocks: 896199
- Forest area: 176426.10 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87507
- Scheduled area: 14862.69 ha
- Eligible blocks (age class >= 40): 875068
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.78 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 26.81 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
