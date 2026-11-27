# WS4 tiled 30-m dataset — I2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S12` (parent `I2|BC`)
- Tile / row / col: `I2` / 1 / 2
- Province: `BC`
- Centroid: 51.486538, -127.175746
- Allocated harvest: 103508.427999 m3
- Productive subcell area: 140680.462759 ha
- Committed geometry area: 207359.007330 ha
- Clipped inventory geometry: 207359.007330 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2069218
- Blocks: 988620
- Forest area: 186229.62 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 96659
- Scheduled area: 16988.40 ha
- Eligible blocks (age class >= 40): 966590
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 27.77 MB
- Schedules: 1.15 MB
- Runs: 0.00 MB
- Total: 28.92 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
