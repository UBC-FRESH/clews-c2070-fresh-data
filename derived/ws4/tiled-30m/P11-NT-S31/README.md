# WS4 tiled 30-m dataset — P11|NT|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `P11|NT|S31` (parent `P11|NT`)
- Tile / row / col: `P11` / 3 / 1
- Province: `NT`
- Centroid: 65.883508, -114.348658
- Allocated harvest: 10.580551 m3
- Productive subcell area: 29842.610873 ha
- Committed geometry area: 168420.111543 ha
- Clipped inventory geometry: 168420.111543 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 912843
- Blocks: 434189
- Forest area: 82155.87 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 31111
- Scheduled area: 5367.78 ha
- Eligible blocks (age class >= 40): 311104
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 12.69 MB
- Schedules: 0.37 MB
- Runs: 0.00 MB
- Total: 13.05 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
