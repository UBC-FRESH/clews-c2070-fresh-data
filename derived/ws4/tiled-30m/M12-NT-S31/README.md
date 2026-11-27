# WS4 tiled 30-m dataset — M12|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `M12|NT|S31` (parent `M12|NT`)
- Tile / row / col: `M12` / 3 / 1
- Province: `NT`
- Centroid: 62.265435, -108.719549
- Allocated harvest: 33.870480 m3
- Productive subcell area: 93691.747566 ha
- Committed geometry area: 250000.000000 ha
- Clipped inventory geometry: 250000.000000 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1476505
- Blocks: 525878
- Forest area: 132885.45 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 37466
- Scheduled area: 6839.64 ha
- Eligible blocks (age class >= 40): 374660
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 17.19 MB
- Schedules: 0.44 MB
- Runs: 0.00 MB
- Total: 17.64 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
