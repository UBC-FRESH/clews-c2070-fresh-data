# WS4 tiled 30-m dataset — E16|MB|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `E16|MB|S33` (parent `E16|MB`)
- Tile / row / col: `E16` / 3 / 3
- Province: `MB`
- Centroid: 51.933686, -95.156665
- Allocated harvest: 82.993221 m3
- Productive subcell area: 1852.374884 ha
- Committed geometry area: 2454.772112 ha
- Clipped inventory geometry: 2454.772112 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 19825
- Blocks: 5547
- Forest area: 1784.25 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 3694
- Scheduled area: 956.70 ha
- Eligible blocks (age class >= 40): 3694
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.33 MB
- Schedules: 0.04 MB
- Runs: 0.00 MB
- Total: 0.36 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
