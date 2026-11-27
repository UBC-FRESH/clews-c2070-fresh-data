# WS4 tiled 30-m dataset — G2|BC|S11

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `G2|BC|S11` (parent `G2|BC`)
- Tile / row / col: `G2` / 1 / 1
- Province: `BC`
- Centroid: 49.092154, -125.825821
- Allocated harvest: 2822.323258 m3
- Productive subcell area: 2776.972732 ha
- Committed geometry area: 3056.159842 ha
- Clipped inventory geometry: 3056.159842 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 32558
- Blocks: 16682
- Forest area: 2930.22 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 1642
- Scheduled area: 285.12 ha
- Eligible blocks (age class >= 40): 16411
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 0.65 MB
- Schedules: 0.02 MB
- Runs: 0.00 MB
- Total: 0.67 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
