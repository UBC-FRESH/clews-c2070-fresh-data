# WS4 tiled 30-m dataset — J13|SK|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `J13|SK|S21` (parent `J13|SK`)
- Tile / row / col: `J13` / 2 / 1
- Province: `SK`
- Centroid: 57.971194, -104.321734
- Allocated harvest: 12328.514886 m3
- Productive subcell area: 149350.626558 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1491187
- Blocks: 247393
- Forest area: 134206.83 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 17086
- Scheduled area: 7722.45 ha
- Eligible blocks (age class >= 40): 170855
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 13.38 MB
- Schedules: 0.20 MB
- Runs: 0.00 MB
- Total: 13.58 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
