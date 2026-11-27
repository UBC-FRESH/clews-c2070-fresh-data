# WS4 tiled 30-m dataset — H35|NL|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `H35|NL|S31` (parent `H35|NL`)
- Tile / row / col: `H35` / 3 / 1
- Province: `NL`
- Centroid: 48.013419, -55.629891
- Allocated harvest: 8749.123122 m3
- Productive subcell area: 118025.341165 ha
- Committed geometry area: 246419.835807 ha
- Clipped inventory geometry: 246419.835807 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1474845
- Blocks: 844841
- Forest area: 132736.05 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 75845
- Scheduled area: 11726.37 ha
- Eligible blocks (age class >= 40): 758450
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 22.33 MB
- Schedules: 0.90 MB
- Runs: 0.00 MB
- Total: 23.23 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
