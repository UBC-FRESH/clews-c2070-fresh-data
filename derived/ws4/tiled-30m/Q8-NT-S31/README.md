# WS4 tiled 30-m dataset — Q8|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q8|NT|S31` (parent `Q8|NT`)
- Tile / row / col: `Q8` / 3 / 1
- Province: `NT`
- Centroid: 65.654153, -124.904655
- Allocated harvest: 85.018287 m3
- Productive subcell area: 138418.897170 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1813750
- Blocks: 575033
- Forest area: 163237.50 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 45836
- Scheduled area: 10484.28 ha
- Eligible blocks (age class >= 40): 458360
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 20.69 MB
- Schedules: 0.54 MB
- Runs: 0.00 MB
- Total: 21.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
