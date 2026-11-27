# WS4 tiled 30-m dataset — K29|NL|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|NL|S33` (parent `K29|NL`)
- Tile / row / col: `K29` / 3 / 3
- Province: `NL`
- Centroid: 55.369871, -61.926196
- Allocated harvest: 5634.433291 m3
- Productive subcell area: 117739.178400 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1201570
- Blocks: 526501
- Forest area: 108141.30 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 40814
- Scheduled area: 8259.75 ha
- Eligible blocks (age class >= 40): 408132
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 16.19 MB
- Schedules: 0.48 MB
- Runs: 0.00 MB
- Total: 16.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
