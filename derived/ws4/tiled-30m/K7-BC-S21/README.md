# WS4 tiled 30-m dataset — K7|BC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K7|BC|S21` (parent `K7|BC`)
- Tile / row / col: `K7` / 2 / 1
- Province: `BC`
- Centroid: 57.082883, -120.154702
- Allocated harvest: 33880.804210 m3
- Productive subcell area: 84585.356360 ha
- Committed geometry area: 89110.228137 ha
- Clipped inventory geometry: 89110.228137 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 947459
- Blocks: 304867
- Forest area: 85271.31 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29114
- Scheduled area: 7017.75 ha
- Eligible blocks (age class >= 40): 291135
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.00 MB
- Schedules: 0.34 MB
- Runs: 0.00 MB
- Total: 11.34 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
