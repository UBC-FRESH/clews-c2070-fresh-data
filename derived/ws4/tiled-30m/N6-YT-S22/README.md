# WS4 tiled 30-m dataset — N6|YT|S22

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `N6|YT|S22` (parent `N6|YT`)
- Tile / row / col: `N6` / 2 / 2
- Province: `YT`
- Centroid: 60.479475, -124.852543
- Allocated harvest: 493.404432 m3
- Productive subcell area: 207771.493979 ha
- Committed geometry area: 239994.627539 ha
- Clipped inventory geometry: 239994.627539 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2178837
- Blocks: 1035413
- Forest area: 196095.33 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 95097
- Scheduled area: 16478.82 ha
- Eligible blocks (age class >= 40): 950967
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 29.65 MB
- Schedules: 1.13 MB
- Runs: 0.00 MB
- Total: 30.78 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
