# WS4 tiled 30-m dataset — K11|SK|S13

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|SK|S13` (parent `K11|SK`)
- Tile / row / col: `K11` / 1 / 3
- Province: `SK`
- Centroid: 58.555868, -108.071038
- Allocated harvest: 13857.927805 m3
- Productive subcell area: 137192.076620 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1450434
- Blocks: 392515
- Forest area: 130539.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 29883
- Scheduled area: 8542.53 ha
- Eligible blocks (age class >= 40): 298826
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 15.41 MB
- Schedules: 0.35 MB
- Runs: 0.00 MB
- Total: 15.76 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
