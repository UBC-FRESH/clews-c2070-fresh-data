# WS4 tiled 30-m dataset — K13|SK|S31

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K13|SK|S31` (parent `K13|SK`)
- Tile / row / col: `K13` / 3 / 1
- Province: `SK`
- Centroid: 59.782321, -104.864509
- Allocated harvest: 12713.114479 m3
- Productive subcell area: 134335.644414 ha
- Committed geometry area: 237101.745095 ha
- Clipped inventory geometry: 237101.745095 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 1370677
- Blocks: 338777
- Forest area: 123360.93 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 22488
- Scheduled area: 5004.00 ha
- Eligible blocks (age class >= 40): 224871
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 14.05 MB
- Schedules: 0.26 MB
- Runs: 0.00 MB
- Total: 14.31 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
