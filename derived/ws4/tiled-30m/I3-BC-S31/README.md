# WS4 tiled 30-m dataset — I3|BC|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `I3|BC|S31` (parent `I3|BC`)
- Tile / row / col: `I3` / 3 / 1
- Province: `BC`
- Centroid: 52.657848, -126.766986
- Allocated harvest: 84576.456551 m3
- Productive subcell area: 172141.601685 ha
- Committed geometry area: 239949.321866 ha
- Clipped inventory geometry: 239949.321866 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1549842
- Blocks: 921202
- Forest area: 139485.78 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 86353
- Scheduled area: 12489.39 ha
- Eligible blocks (age class >= 40): 863523
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 23.36 MB
- Schedules: 1.03 MB
- Runs: 0.00 MB
- Total: 24.39 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
