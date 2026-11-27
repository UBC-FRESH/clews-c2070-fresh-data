# WS4 tiled 30-m dataset — Q11|NT|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q11|NT|S11` (parent `Q11|NT`)
- Tile / row / col: `Q11` / 1 / 1
- Province: `NT`
- Centroid: 66.184075, -114.877451
- Allocated harvest: 4.080618 m3
- Productive subcell area: 9893.261404 ha
- Committed geometry area: 23741.803362 ha
- Clipped inventory geometry: 23741.803362 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 67041
- Blocks: 34940
- Forest area: 6033.69 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1866
- Scheduled area: 234.63 ha
- Eligible blocks (age class >= 40): 18654
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 1.24 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 1.26 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
