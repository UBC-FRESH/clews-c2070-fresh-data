# WS4 tiled 30-m dataset — Q10|NT|S23

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `Q10|NT|S23` (parent `Q10|NT`)
- Tile / row / col: `Q10` / 2 / 3
- Province: `NT`
- Centroid: 66.570848, -116.270948
- Allocated harvest: 13.448908 m3
- Productive subcell area: 31266.259774 ha
- Committed geometry area: 95165.545326 ha
- Clipped inventory geometry: 95165.545326 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 274507
- Blocks: 153977
- Forest area: 24705.63 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 8032
- Scheduled area: 974.16 ha
- Eligible blocks (age class >= 40): 80319
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 4.79 MB
- Schedules: 0.09 MB
- Runs: 0.00 MB
- Total: 4.88 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
