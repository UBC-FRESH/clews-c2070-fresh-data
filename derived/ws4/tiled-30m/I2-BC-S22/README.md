# WS4 tiled 30-m dataset — I2|BC|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I2|BC|S22` (parent `I2|BC`)
- Tile / row / col: `I2` / 2 / 2
- Province: `BC`
- Centroid: 51.828458, -127.665886
- Allocated harvest: 93172.247417 m3
- Productive subcell area: 126632.344208 ha
- Committed geometry area: 186652.479498 ha
- Clipped inventory geometry: 186652.479498 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1918232
- Blocks: 888312
- Forest area: 172640.88 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 87647
- Scheduled area: 16022.88 ha
- Eligible blocks (age class >= 40): 876461
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 25.65 MB
- Schedules: 1.04 MB
- Runs: 0.00 MB
- Total: 26.69 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
