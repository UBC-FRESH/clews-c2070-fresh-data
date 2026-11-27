# WS4 tiled 30-m dataset — K2|BC|S12

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K2|BC|S12` (parent `K2|BC`)
- Tile / row / col: `K2` / 1 / 2
- Province: `BC`
- Centroid: 53.786134, -129.597701
- Allocated harvest: 120014.875064 m3
- Productive subcell area: 168316.246307 ha
- Committed geometry area: 239216.445583 ha
- Clipped inventory geometry: 239216.445583 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1801505
- Blocks: 1021967
- Forest area: 162135.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 97581
- Scheduled area: 15117.84 ha
- Eligible blocks (age class >= 40): 975802
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 26.36 MB
- Schedules: 1.16 MB
- Runs: 0.00 MB
- Total: 27.52 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
