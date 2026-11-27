# WS4 tiled 30-m dataset — K13|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S21` (parent `K13|SK`)
- Tile / row / col: `K13` / 2 / 1
- Province: `SK`
- Centroid: 59.338534, -104.717375
- Allocated harvest: 13404.703615 m3
- Productive subcell area: 141643.458128 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1706461
- Blocks: 386726
- Forest area: 153581.49 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 20672
- Scheduled area: 4339.98 ha
- Eligible blocks (age class >= 40): 206718
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.96 MB
- Schedules: 0.24 MB
- Runs: 0.00 MB
- Total: 17.20 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
