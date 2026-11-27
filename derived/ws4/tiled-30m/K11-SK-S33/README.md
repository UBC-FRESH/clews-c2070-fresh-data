# WS4 tiled 30-m dataset — K11|SK|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K11|SK|S33` (parent `K11|SK`)
- Tile / row / col: `K11` / 3 / 3
- Province: `SK`
- Centroid: 59.458229, -108.440970
- Allocated harvest: 13857.927805 m3
- Productive subcell area: 137192.076620 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1154534
- Blocks: 331668
- Forest area: 103908.06 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 25889
- Scheduled area: 4419.90 ha
- Eligible blocks (age class >= 40): 258883
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.71 MB
- Schedules: 0.30 MB
- Runs: 0.00 MB
- Total: 13.01 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
