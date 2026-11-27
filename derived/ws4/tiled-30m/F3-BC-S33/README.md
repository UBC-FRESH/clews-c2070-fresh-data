# WS4 tiled 30-m dataset — F3|BC|S33

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `F3|BC|S33` (parent `F3|BC`)
- Tile / row / col: `F3` / 3 / 3
- Province: `BC`
- Centroid: 49.424767, -122.581893
- Allocated harvest: 167956.858498 m3
- Productive subcell area: 167297.544505 ha
- Committed geometry area: 247803.518729 ha
- Clipped inventory geometry: 247803.518729 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 2057583
- Blocks: 1206821
- Forest area: 185182.47 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 114710
- Scheduled area: 16978.68 ha
- Eligible blocks (age class >= 40): 1147091
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 31.10 MB
- Schedules: 1.38 MB
- Runs: 0.00 MB
- Total: 32.49 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
