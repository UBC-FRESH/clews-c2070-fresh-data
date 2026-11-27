# WS4 tiled 30-m dataset — I10|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I10|SK|S13` (parent `I10|SK`)
- Tile / row / col: `I10` / 1 / 3
- Province: `SK`
- Centroid: 55.565620, -109.456424
- Allocated harvest: 40818.331291 m3
- Productive subcell area: 210926.021089 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1975103
- Blocks: 563020
- Forest area: 177759.27 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 32050
- Scheduled area: 7425.27 ha
- Eligible blocks (age class >= 40): 320492
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 21.25 MB
- Schedules: 0.38 MB
- Runs: 0.00 MB
- Total: 21.62 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
