# WS4 tiled 30-m dataset — K29|QC|S21

This is a real compiled WS4 dataset built from 30-m SCANFI pixels for
one 50-km supply node. It is a `model_estimate` / `sensitivity_only`
artifact, not official OSeCAN and not a chain v5.1 change.

## Identity

- Node: `K29|QC|S21` (parent `K29|QC`)
- Tile / row / col: `K29` / 2 / 1
- Province: `QC`
- Centroid: 55.397992, -63.830978
- Allocated harvest: 13664.261300 m3
- Productive subcell area: 82991.012036 ha
- Committed geometry area: 171512.131278 ha
- Clipped inventory geometry: 171512.131278 ha

## Inventory

- Inventory resolution: 30 m (0.09 ha per fragment)
- Tile resolution: 30,000 m
- Connectivity: 8-neighbour cliques of equal `(age_class, curve_key)`
- Forest fragments: 778586
- Blocks: 447791
- Forest area: 70072.74 ha

## Validation and simulation

- `ws4 validate`: pass
- Schedule rows: 36279
- Scheduled area: 5212.98 ha
- Eligible blocks (age class >= 40): 362786
- Simulation: not_run_datasets_only (--datasets-only)

## Storage

- Dataset: 11.85 MB
- Schedules: 0.43 MB
- Runs: 0.00 MB
- Total: 12.27 MB

The managed track shares the natural RSYC curve: there is no
planting yield-response data in this build. No operability, tenure,
road, mill, or policy claim is made.

See `inventory_summary.json` for exclusions, curve diagnostics,
clique sizes, validation output, and simulation totals.
